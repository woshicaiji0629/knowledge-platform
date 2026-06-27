import asyncio
import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, cast

from knowledge_platform.embeddings.base import EmbeddingBatch, EmbeddingProvider, TextEmbedding

DEFAULT_DASHSCOPE_EMBEDDING_ENDPOINT = "https://dashscope.aliyuncs.com/compatible-mode/v1/embeddings"
DEFAULT_DASHSCOPE_EMBEDDING_MODEL = "text-embedding-v4"


@dataclass(frozen=True)
class DashScopeEmbeddingConfig:
    api_key: str
    model: str = DEFAULT_DASHSCOPE_EMBEDDING_MODEL
    endpoint: str = DEFAULT_DASHSCOPE_EMBEDDING_ENDPOINT
    timeout_seconds: float = 60.0


class DashScopeEmbeddingProvider(EmbeddingProvider):
    def __init__(self, config: DashScopeEmbeddingConfig) -> None:
        if not config.api_key:
            raise ValueError("DashScope API key is required")
        self._config = config

    async def embed_texts(self, texts: list[str]) -> list[TextEmbedding]:
        batch = await self.embed_texts_with_metadata(texts)
        return batch.embeddings

    async def embed_texts_with_metadata(self, texts: list[str]) -> EmbeddingBatch:
        if not texts:
            return EmbeddingBatch(embeddings=[], request_id="", usage={})
        return await asyncio.to_thread(self._embed_texts_sync, texts)

    def _embed_texts_sync(self, texts: list[str]) -> EmbeddingBatch:
        payload = json.dumps({"model": self._config.model, "input": texts}).encode("utf-8")
        request = urllib.request.Request(
            self._config.endpoint,
            data=payload,
            headers={
                "Authorization": f"Bearer {self._config.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self._config.timeout_seconds) as response:
                response_body = response.read().decode("utf-8")
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"DashScope embedding request failed: HTTP {error.code}: {body}") from error
        except urllib.error.URLError as error:
            raise RuntimeError(f"DashScope embedding request failed: {error.reason}") from error

        response_data = json.loads(response_body)
        request_id = _string_value(response_data.get("request_id")) or _string_value(response_data.get("id"))
        usage = _usage(response_data.get("usage"))
        data = response_data.get("data")
        if not isinstance(data, list):
            raise RuntimeError("DashScope embedding response missing data list")

        embeddings: list[TextEmbedding] = []
        for item in cast(list[object], data):
            if not isinstance(item, dict):
                continue
            item_data = cast(dict[object, object], item)
            embedding = item_data.get("embedding")
            index = item_data.get("index")
            if not isinstance(embedding, list) or not isinstance(index, int):
                continue
            embeddings.append(
                TextEmbedding(
                    text_index=index,
                    vector=[float(value) for value in cast(list[Any], embedding)],
                )
            )

        embeddings.sort(key=lambda embedding: embedding.text_index)
        if len(embeddings) != len(texts):
            raise RuntimeError(f"DashScope returned {len(embeddings)} embeddings for {len(texts)} texts")
        return EmbeddingBatch(embeddings=embeddings, request_id=request_id, usage=usage)


def dashscope_config_from_env() -> DashScopeEmbeddingConfig:
    api_key = os.environ.get("DASHSCOPE_API_KEY", "")
    model = os.environ.get("DASHSCOPE_EMBEDDING_MODEL", DEFAULT_DASHSCOPE_EMBEDDING_MODEL)
    endpoint = os.environ.get("DASHSCOPE_EMBEDDING_ENDPOINT", DEFAULT_DASHSCOPE_EMBEDDING_ENDPOINT)
    timeout_seconds = float(os.environ.get("DASHSCOPE_EMBEDDING_TIMEOUT_SECONDS", "60"))
    return DashScopeEmbeddingConfig(
        api_key=api_key,
        model=model,
        endpoint=endpoint,
        timeout_seconds=timeout_seconds,
    )


def _string_value(value: object) -> str:
    return value if isinstance(value, str) else ""


def _usage(value: object) -> dict[str, int]:
    if not isinstance(value, dict):
        return {}
    usage_data = cast(dict[object, object], value)
    usage: dict[str, int] = {}
    for key, raw_value in usage_data.items():
        if isinstance(key, str) and isinstance(raw_value, int):
            usage[key] = raw_value
    return usage
