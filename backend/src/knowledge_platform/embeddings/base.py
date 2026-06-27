from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class TextEmbedding:
    text_index: int
    vector: list[float]


@dataclass(frozen=True)
class EmbeddingBatch:
    embeddings: list[TextEmbedding]
    request_id: str
    usage: dict[str, int]


class EmbeddingProvider(ABC):
    @abstractmethod
    async def embed_texts(self, texts: list[str]) -> list[TextEmbedding]:
        raise NotImplementedError
