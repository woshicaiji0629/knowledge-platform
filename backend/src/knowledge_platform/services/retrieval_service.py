from dataclasses import dataclass
from typing import Protocol

from knowledge_platform.embeddings.dashscope import DashScopeEmbeddingProvider
from knowledge_platform.sessions.models import Citation
from knowledge_platform.vectorstores.base import VectorStore
from knowledge_platform.vectorstores.qdrant import QdrantVectorStore


@dataclass(frozen=True)
class RetrievalContext:
    context_text: str
    citations: list[Citation]


class RetrievalServiceProtocol(Protocol):
    async def retrieve(self, query: str, limit: int | None = None) -> RetrievalContext:
        raise NotImplementedError


class RetrievalService:
    def __init__(self, vector_store: VectorStore, default_limit: int = 5, context_max_chars: int = 6000) -> None:
        self._vector_store = vector_store
        self._default_limit = default_limit
        self._context_max_chars = context_max_chars

    async def retrieve(self, query: str, limit: int | None = None) -> RetrievalContext:
        results = self._vector_store.search(query=query, limit=limit or self._default_limit)
        citations = [
            Citation(
                title=result.chunk.title,
                url=result.chunk.url,
                source=result.chunk.source,
                score=result.score,
            )
            for result in results
        ]
        context_text = _truncate_context(
            "\n\n".join(result.chunk.content for result in results),
            self._context_max_chars,
        )
        return RetrievalContext(context_text=context_text, citations=citations)


class QdrantRetrievalService:
    def __init__(
        self,
        embedding_provider: DashScopeEmbeddingProvider,
        vector_store: QdrantVectorStore,
        default_limit: int = 5,
        context_max_chars: int = 6000,
    ) -> None:
        self._embedding_provider = embedding_provider
        self._vector_store = vector_store
        self._default_limit = default_limit
        self._context_max_chars = context_max_chars

    async def retrieve(self, query: str, limit: int | None = None) -> RetrievalContext:
        embedding_batch = await self._embedding_provider.embed_texts_with_metadata([query])
        if not embedding_batch.embeddings:
            return RetrievalContext(context_text="", citations=[])

        results = await self._vector_store.search_points(
            vector=embedding_batch.embeddings[0].vector,
            limit=limit or self._default_limit,
        )
        citations = [
            Citation(
                title=str(result.payload.get("title", "")),
                url=str(result.payload.get("source_url", "")),
                source=str(result.payload.get("source", "aliyun_docs") or "aliyun_docs"),
                score=result.score,
            )
            for result in results
        ]
        context_text = _truncate_context(
            "\n\n".join(_context_chunk(result.payload) for result in results),
            self._context_max_chars,
        )
        return RetrievalContext(context_text=context_text, citations=citations)


def _context_chunk(payload: dict[str, object]) -> str:
    title = str(payload.get("title", ""))
    source_url = str(payload.get("source_url", ""))
    heading_path = str(payload.get("heading_path", ""))
    content = str(payload.get("content", ""))
    header_parts = [part for part in [title, heading_path, source_url] if part]
    header = "\n".join(header_parts)
    return f"{header}\n{content}".strip()


def _truncate_context(context_text: str, max_chars: int) -> str:
    if max_chars <= 0 or len(context_text) <= max_chars:
        return context_text
    return context_text[:max_chars].rstrip()
