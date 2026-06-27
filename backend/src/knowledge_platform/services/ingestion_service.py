from dataclasses import dataclass

from knowledge_platform.crawlers.aliyun_docs import AliyunDocsCrawler
from knowledge_platform.crawlers.base import CrawlPlan, CrawlRequest
from knowledge_platform.documents.models import RawDocument


@dataclass(frozen=True)
class IngestionPlanResult:
    plan: CrawlPlan
    status: str
    message: str


@dataclass(frozen=True)
class IngestionCrawlResult:
    documents: list[RawDocument]
    status: str
    message: str


class IngestionService:
    def __init__(self, aliyun_docs_crawler: AliyunDocsCrawler) -> None:
        self._aliyun_docs_crawler = aliyun_docs_crawler

    def plan_aliyun_docs_ingestion(self, seed_urls: list[str], max_pages: int, max_depth: int) -> IngestionPlanResult:
        plan = self._aliyun_docs_crawler.build_plan(
            CrawlRequest(seed_urls=seed_urls, max_pages=max_pages, max_depth=max_depth)
        )
        return IngestionPlanResult(
            plan=plan,
            status="planned",
            message="已生成采集计划；真实爬取、文本清洗、切块、embedding 和向量库写入将在后续阶段实现。",
        )

    def crawl_aliyun_docs(self, seed_urls: list[str], max_pages: int, max_depth: int) -> IngestionCrawlResult:
        documents = self._aliyun_docs_crawler.crawl(
            CrawlRequest(seed_urls=seed_urls, max_pages=max_pages, max_depth=max_depth)
        )
        return IngestionCrawlResult(
            documents=documents,
            status="completed",
            message=f"已抓取 {len(documents)} 篇阿里云文档，并保存到独立数据源目录。",
        )
