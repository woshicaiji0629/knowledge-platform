import asyncio

from knowledge_platform.llm.intent import RuleBasedIntentClassifier
from knowledge_platform.services.chat_service import ChatService
from knowledge_platform.services.retrieval_service import RetrievalContext
from knowledge_platform.sessions.models import Citation
from knowledge_platform.sessions.store import InMemorySessionStore


class FakeRetrievalService:
    async def retrieve(self, query: str, limit: int | None = None) -> RetrievalContext:
        return RetrievalContext(
            context_text=f"context for {query}",
            citations=[
                Citation(
                    title="ECS product overview",
                    url="https://help.aliyun.com/ecs",
                    source="aliyun_docs",
                    score=0.8,
                )
            ],
        )


def test_chat_service_uses_async_retrieval_context() -> None:
    service = ChatService(
        session_store=InMemorySessionStore(),
        retrieval_service=FakeRetrievalService(),
        intent_classifier=RuleBasedIntentClassifier(),
    )

    result = asyncio.run(service.send_message(session_id="session-1", message="ECS 怎么选型"))

    assert result.assistant_message.citations[0].title == "ECS product overview"
    assert result.assistant_message.content == "已根据本地文档索引生成占位回答。问题：ECS 怎么选型"
    assert len(result.session.messages) == 2
