from abc import ABC, abstractmethod
from dataclasses import dataclass

from knowledge_platform.documents.models import RawDocument


@dataclass(frozen=True)
class CrawlRequest:
    seed_urls: list[str]
    max_pages: int = 20
    max_depth: int = 1


@dataclass(frozen=True)
class CrawlPlan:
    source: str
    seed_urls: list[str]
    allowed_domains: list[str]
    max_pages: int
    max_depth: int


class DocumentCrawler(ABC):
    @abstractmethod
    def build_plan(self, request: CrawlRequest) -> CrawlPlan:
        raise NotImplementedError

    @abstractmethod
    def crawl(self, request: CrawlRequest) -> list[RawDocument]:
        raise NotImplementedError
