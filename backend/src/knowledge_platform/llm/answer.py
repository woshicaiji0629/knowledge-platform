import asyncio
import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Protocol, cast

from knowledge_platform.sessions.models import Citation

DEFAULT_DASHSCOPE_CHAT_ENDPOINT = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
DEFAULT_DASHSCOPE_CHAT_MODEL = "qwen-turbo"


@dataclass(frozen=True)
class AnswerGenerationRequest:
    question: str
    context_text: str
    citations: list[Citation]


class AnswerGeneratorProtocol(Protocol):
    async def generate(self, request: AnswerGenerationRequest) -> str:
        raise NotImplementedError


class SkeletonAnswerGenerator:
    async def generate(self, request: AnswerGenerationRequest) -> str:
        if request.context_text:
            return f"已根据本地文档索引生成占位回答。问题：{request.question}"
        return "当前还没有可用的本地文档索引。请先运行阿里云官方文档采集和入库流程。"


@dataclass(frozen=True)
class DashScopeChatConfig:
    api_key: str
    model: str = DEFAULT_DASHSCOPE_CHAT_MODEL
    endpoint: str = DEFAULT_DASHSCOPE_CHAT_ENDPOINT
    timeout_seconds: float = 60.0
    max_tokens: int = 1200
    temperature: float = 0.2


class DashScopeAnswerGenerator:
    def __init__(self, config: DashScopeChatConfig) -> None:
        if not config.api_key:
            raise ValueError("DashScope API key is required")
        self._config = config

    async def generate(self, request: AnswerGenerationRequest) -> str:
        if not request.context_text:
            return "当前没有检索到足够的本地文档依据，无法给出可靠回答。"
        return await asyncio.to_thread(self._generate_sync, request)

    def _generate_sync(self, request: AnswerGenerationRequest) -> str:
        payload = json.dumps(
            {
                "model": self._config.model,
                "messages": [
                    {"role": "system", "content": _system_prompt()},
                    {"role": "user", "content": _user_prompt(request)},
                ],
                "temperature": self._config.temperature,
                "max_tokens": self._config.max_tokens,
            },
            ensure_ascii=False,
        ).encode("utf-8")
        http_request = urllib.request.Request(
            self._config.endpoint,
            data=payload,
            headers={
                "Authorization": f"Bearer {self._config.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(http_request, timeout=self._config.timeout_seconds) as response:
                response_body = response.read().decode("utf-8")
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"DashScope answer generation failed: HTTP {error.code}: {body}") from error
        except urllib.error.URLError as error:
            raise RuntimeError(f"DashScope answer generation failed: {error.reason}") from error

        response_data = json.loads(response_body)
        if not isinstance(response_data, dict):
            raise RuntimeError("DashScope answer generation response is invalid")
        response_object = cast(dict[object, object], response_data)
        choices = response_object.get("choices")
        if not isinstance(choices, list) or not choices:
            raise RuntimeError("DashScope answer generation response missing choices")

        first_choice = cast(list[object], choices)[0]
        if not isinstance(first_choice, dict):
            raise RuntimeError("DashScope answer generation response choice is invalid")
        message = cast(dict[object, object], first_choice).get("message")
        if not isinstance(message, dict):
            raise RuntimeError("DashScope answer generation response missing message")
        content = cast(dict[object, object], message).get("content")
        if not isinstance(content, str) or not content.strip():
            raise RuntimeError("DashScope answer generation response missing content")
        return content.strip()


def dashscope_chat_config_from_env() -> DashScopeChatConfig:
    return DashScopeChatConfig(
        api_key=os.environ.get("DASHSCOPE_API_KEY", ""),
        model=os.environ.get("DASHSCOPE_CHAT_MODEL", DEFAULT_DASHSCOPE_CHAT_MODEL),
        endpoint=os.environ.get("DASHSCOPE_CHAT_ENDPOINT", DEFAULT_DASHSCOPE_CHAT_ENDPOINT),
        timeout_seconds=float(os.environ.get("DASHSCOPE_CHAT_TIMEOUT_SECONDS", "60")),
        max_tokens=int(os.environ.get("DASHSCOPE_CHAT_MAX_TOKENS", "1200")),
        temperature=float(os.environ.get("DASHSCOPE_CHAT_TEMPERATURE", "0.2")),
    )


def _system_prompt() -> str:
    return (
        "你是一个面向产品选型和产品使用的阿里云官方文档问答助手。"
        "只能基于用户提供的检索上下文回答；不要编造文档中没有的信息。"
        "回答要偏产品导向，优先解释适用场景、关键能力、限制和下一步建议。"
        "如果上下文不足，明确说明缺少依据。"
    )


def _user_prompt(request: AnswerGenerationRequest) -> str:
    citation_lines = [
        f"[{index}] {citation.title} {citation.url}".strip()
        for index, citation in enumerate(request.citations, start=1)
    ]
    citations_text = "\n".join(citation_lines) if citation_lines else "无"
    return (
        f"问题：\n{request.question}\n\n"
        f"检索上下文：\n{request.context_text}\n\n"
        f"引用来源：\n{citations_text}\n\n"
        "请用中文回答。尽量结构化，但不要输出没有依据的 API 参数细节。"
    )
