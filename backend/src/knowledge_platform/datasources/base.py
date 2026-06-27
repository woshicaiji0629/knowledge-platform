from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class SourceDocument:
    id: str
    title: str
    content: str
    source: str


class DataSource(ABC):
    @abstractmethod
    def search(self, query: str, limit: int = 5) -> list[SourceDocument]:
        raise NotImplementedError
