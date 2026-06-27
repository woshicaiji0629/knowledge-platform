from dataclasses import dataclass

from knowledge_platform.sessions.models import Citation
from knowledge_platform.vectorstores.base import VectorStore


@dataclass(frozen=True)
class RetrievalContext:
    context_text: str
    citations: list[Citation]


class RetrievalService:
    def __init__(self, vector_store: VectorStore) -> None:
        self._vector_store = vector_store

    def retrieve(self, query: str, limit: int = 5) -> RetrievalContext:
        results = self._vector_store.search(query=query, limit=limit)
        citations = [
            Citation(
                title=result.chunk.title,
                url=result.chunk.url,
                source=result.chunk.source,
                score=result.score,
            )
            for result in results
        ]
        context_text = "\n\n".join(result.chunk.content for result in results)
        return RetrievalContext(context_text=context_text, citations=citations)
