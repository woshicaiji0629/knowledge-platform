from abc import ABC, abstractmethod
from dataclasses import dataclass

from knowledge_platform.documents.models import DocumentChunk


@dataclass(frozen=True)
class VectorSearchResult:
    chunk: DocumentChunk
    score: float


class VectorStore(ABC):
    @abstractmethod
    def upsert(self, chunks: list[DocumentChunk]) -> int:
        raise NotImplementedError

    @abstractmethod
    def search(self, query: str, limit: int = 5) -> list[VectorSearchResult]:
        raise NotImplementedError
