from knowledge_platform.documents.models import DocumentChunk
from knowledge_platform.vectorstores.base import VectorSearchResult, VectorStore


class MemoryVectorStore(VectorStore):
    def __init__(self) -> None:
        self._chunks: dict[str, DocumentChunk] = {}

    def upsert(self, chunks: list[DocumentChunk]) -> int:
        for chunk in chunks:
            self._chunks[chunk.id] = chunk
        return len(chunks)

    def search(self, query: str, limit: int = 5) -> list[VectorSearchResult]:
        query_terms = set(query.lower().split())
        if not query_terms:
            return []

        results: list[VectorSearchResult] = []
        for chunk in self._chunks.values():
            content_terms = set(chunk.content.lower().split())
            score = len(query_terms.intersection(content_terms)) / len(query_terms)
            if score > 0:
                results.append(VectorSearchResult(chunk=chunk, score=score))

        results.sort(key=lambda result: result.score, reverse=True)
        return results[:limit]
