import json
import re
import time
from collections import Counter, deque
from concurrent.futures import FIRST_COMPLETED, Future, ThreadPoolExecutor, wait
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, TypedDict, cast

from knowledge_platform.crawlers.aliyun_docs import (
    AliyunAntiBotPageError,
    AliyunDocsCrawler,
    CrawledPage,
    is_aliyun_anti_bot_page,
)
from knowledge_platform.documents.models import RawDocument


class ProductSeed(TypedDict):
    product: str
    urls: list[str]


@dataclass(frozen=True)
class QueuedUrl:
    url: str
    depth: int
    attempt: int = 0


@dataclass(frozen=True)
class ProductCrawlReport:
    product: str
    crawled: int
    anti_bot: int
    failed: int
    retried: int
    remaining_retry_urls: list[str]


def main() -> None:
    repo_root = Path(__file__).resolve().parents[4]
    seeds_path = repo_root / "data" / "datasources" / "aliyun-docs" / "seeds.json"
    seeds = json.loads(seeds_path.read_text(encoding="utf-8"))
    target_pages_per_product = int(seeds["target_pages_per_product"])
    concurrency = int(seeds["concurrency"])
    max_depth = int(seeds["max_depth"])
    request_delay_seconds = float(seeds.get("request_delay_seconds", 0))
    anti_bot_delay_seconds = float(seeds.get("anti_bot_delay_seconds", 0))
    retry_delay_seconds = float(seeds.get("retry_delay_seconds", request_delay_seconds))
    max_retries = int(seeds.get("max_retries", 0))
    max_retry_urls_per_product = int(seeds.get("max_retry_urls_per_product", 0))
    max_requests_per_product = int(seeds.get("max_requests_per_product", 0))
    exclude_url_patterns = _read_exclude_url_patterns(seeds)
    crawl_products = _read_crawl_products(seeds)
    products = _read_products(seeds)
    if crawl_products:
        products = [product for product in products if product["product"] in crawl_products]

    crawler = AliyunDocsCrawler(data_root=repo_root / "data")
    _sync_manifest_from_metadata(repo_root=repo_root, crawler=crawler)
    crawled_documents: list[RawDocument] = []
    product_reports: list[ProductCrawlReport] = []
    for product in products:
        product_name = product["product"]
        product_documents, product_report = _crawl_product(
            repo_root=repo_root,
            crawler=crawler,
            product=product_name,
            seed_urls=product["urls"],
            target_pages=target_pages_per_product,
            max_depth=max_depth,
            concurrency=concurrency,
            request_delay_seconds=request_delay_seconds,
            anti_bot_delay_seconds=anti_bot_delay_seconds,
            retry_delay_seconds=retry_delay_seconds,
            max_retries=max_retries,
            max_retry_urls_per_product=max_retry_urls_per_product,
            max_requests_per_product=max_requests_per_product,
            exclude_url_patterns=exclude_url_patterns,
        )
        crawled_documents.extend(product_documents)
        product_reports.append(product_report)
        crawler.write_manifest(product_documents)
        _write_crawl_report(repo_root=repo_root, reports=product_reports)
        print(
            f"{product_name}: crawled {len(product_documents)} new documents, "
            f"anti_bot={product_report.anti_bot}, failed={product_report.failed}, "
            f"retry_left={len(product_report.remaining_retry_urls)}",
            flush=True,
        )

    crawler.write_manifest(crawled_documents)
    _write_crawl_report(repo_root=repo_root, reports=product_reports)
    print(f"total: crawled {len(crawled_documents)} new documents")


def _crawl_product(
    repo_root: Path,
    crawler: AliyunDocsCrawler,
    product: str,
    seed_urls: list[str],
    target_pages: int,
    max_depth: int,
    concurrency: int,
    request_delay_seconds: float,
    anti_bot_delay_seconds: float,
    retry_delay_seconds: float,
    max_retries: int,
    max_retry_urls_per_product: int,
    max_requests_per_product: int,
    exclude_url_patterns: list[str],
) -> tuple[list[RawDocument], ProductCrawlReport]:
    known_documents = _manifest_documents(repo_root)
    known_product_urls = {
        document["url"]
        for document in known_documents
        if document.get("product") == product and "url" in document and not _is_anti_bot_manifest_document(document)
    }
    queued_urls = _initial_product_queue(
        repo_root=repo_root,
        product=product,
        seed_urls=seed_urls,
        known_product_urls=known_product_urls,
        max_retry_urls=max_retry_urls_per_product,
        exclude_url_patterns=exclude_url_patterns,
    )
    visited_urls = set(known_product_urls)
    submitted_urls: set[str] = set()
    crawled_documents: list[RawDocument] = []
    failed_urls: list[str] = []
    anti_bot_urls: list[str] = []
    retried_urls: list[str] = []
    remaining_retry_urls: set[str] = set()
    request_count = 0

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures: dict[Future[CrawledPage | None], QueuedUrl] = {}
        while (queued_urls or futures) and len(known_product_urls) + len(crawled_documents) < target_pages:
            while (
                queued_urls
                and len(futures) < concurrency
                and len(known_product_urls) + len(crawled_documents) + len(futures) < target_pages
                and (max_requests_per_product <= 0 or request_count < max_requests_per_product)
            ):
                queued_url = queued_urls.popleft()
                if queued_url.url in visited_urls or queued_url.url in submitted_urls:
                    continue
                if _is_excluded_url(queued_url.url, exclude_url_patterns):
                    continue
                if not crawler.is_allowed_product_url(queued_url.url, product):
                    continue
                submitted_urls.add(queued_url.url)
                print(
                    f"{product}: request {request_count + 1}"
                    f"{f'/{max_requests_per_product}' if max_requests_per_product > 0 else ''} {queued_url.url}",
                    flush=True,
                )
                _sleep(request_delay_seconds)
                request_count += 1
                futures[executor.submit(crawler.crawl_page, queued_url.url)] = queued_url

            if not futures:
                break

            done_futures, _pending_futures = wait(futures.keys(), return_when=FIRST_COMPLETED)
            for future in done_futures:
                queued_url = futures.pop(future)
                visited_urls.add(queued_url.url)
                try:
                    crawled_page = future.result()
                except AliyunAntiBotPageError:
                    anti_bot_urls.append(queued_url.url)
                    print(f"{product}: anti_bot {queued_url.url}", flush=True)
                    if queued_url.attempt < max_retries:
                        retry_url = QueuedUrl(
                            url=queued_url.url,
                            depth=queued_url.depth,
                            attempt=queued_url.attempt + 1,
                        )
                        retried_urls.append(queued_url.url)
                        submitted_urls.discard(queued_url.url)
                        visited_urls.discard(queued_url.url)
                        _sleep(anti_bot_delay_seconds)
                        queued_urls.append(retry_url)
                    else:
                        remaining_retry_urls.add(queued_url.url)
                    continue
                except RuntimeError:
                    failed_urls.append(queued_url.url)
                    print(f"{product}: failed {queued_url.url}", flush=True)
                    if queued_url.attempt < max_retries:
                        retry_url = QueuedUrl(
                            url=queued_url.url,
                            depth=queued_url.depth,
                            attempt=queued_url.attempt + 1,
                        )
                        retried_urls.append(queued_url.url)
                        submitted_urls.discard(queued_url.url)
                        visited_urls.discard(queued_url.url)
                        _sleep(retry_delay_seconds)
                        queued_urls.append(retry_url)
                    else:
                        remaining_retry_urls.add(queued_url.url)
                    continue
                if crawled_page is None:
                    print(f"{product}: skipped {queued_url.url}", flush=True)
                    continue
                if _is_excluded_crawled_page(crawled_page, product, exclude_url_patterns):
                    _delete_crawled_page_files(crawled_page)
                    print(f"{product}: excluded {crawled_page.document.url}", flush=True)
                    continue

                known_product_urls.add(crawled_page.document.url)
                crawled_documents.append(crawled_page.document)
                print(f"{product}: saved {crawled_page.document.url}", flush=True)
                if queued_url.depth >= max_depth:
                    continue
                for link in crawled_page.links:
                    if link in visited_urls or link in submitted_urls:
                        continue
                    if _is_excluded_url(link, exclude_url_patterns):
                        continue
                    if crawler.is_allowed_product_url(link, product):
                        queued_urls.append(QueuedUrl(url=link, depth=queued_url.depth + 1))

    if failed_urls:
        print(f"{product}: failed {len(failed_urls)} urls", flush=True)
    report = ProductCrawlReport(
        product=product,
        crawled=len(crawled_documents),
        anti_bot=len(anti_bot_urls),
        failed=len(failed_urls),
        retried=len(retried_urls),
        remaining_retry_urls=sorted(remaining_retry_urls),
    )
    return crawled_documents, report


def _initial_product_queue(
    repo_root: Path,
    product: str,
    seed_urls: list[str],
    known_product_urls: set[str],
    max_retry_urls: int,
    exclude_url_patterns: list[str],
) -> deque[QueuedUrl]:
    queued_urls: deque[QueuedUrl] = deque()
    for seed_url in seed_urls:
        if seed_url not in known_product_urls and not _is_excluded_url(seed_url, exclude_url_patterns):
            queued_urls.append(QueuedUrl(url=seed_url, depth=0))
    retry_urls = _anti_bot_manifest_urls(repo_root=repo_root, product=product)
    if max_retry_urls > 0:
        retry_urls = retry_urls[:max_retry_urls]
    for retry_url in retry_urls:
        if retry_url not in known_product_urls and not _is_excluded_url(retry_url, exclude_url_patterns):
            queued_urls.append(QueuedUrl(url=retry_url, depth=0))
    for discovered_url in _discover_product_urls(repo_root, product):
        if discovered_url not in known_product_urls and not _is_excluded_url(discovered_url, exclude_url_patterns):
            queued_urls.append(QueuedUrl(url=discovered_url, depth=0))
    return queued_urls


def _read_products(seeds: dict[str, Any]) -> list[ProductSeed]:
    products = seeds.get("products")
    if not isinstance(products, list):
        raise ValueError("seeds.json must contain a products list")

    product_seeds: list[ProductSeed] = []
    product_items = cast(list[object], products)
    for product in product_items:
        if not isinstance(product, dict):
            continue
        product_data = cast(dict[str, object], product)
        product_name = product_data.get("product")
        urls = product_data.get("urls")
        url = product_data.get("url")
        if isinstance(product_name, str) and isinstance(urls, list):
            product_urls = [item for item in cast(list[object], urls) if isinstance(item, str)]
            product_seeds.append({"product": product_name, "urls": product_urls})
        elif isinstance(product_name, str) and isinstance(url, str):
            product_seeds.append({"product": product_name, "urls": [url]})
    return product_seeds


def _read_crawl_products(seeds: dict[str, Any]) -> set[str]:
    products = seeds.get("crawl_products")
    if not isinstance(products, list):
        return set()
    return {item for item in cast(list[object], products) if isinstance(item, str)}


def _read_exclude_url_patterns(seeds: dict[str, Any]) -> list[str]:
    patterns = seeds.get("exclude_url_patterns")
    if not isinstance(patterns, list):
        return []
    return [item for item in cast(list[object], patterns) if isinstance(item, str) and item]


def _is_excluded_url(url: str, exclude_url_patterns: list[str]) -> bool:
    return any(pattern in url for pattern in exclude_url_patterns)


def is_excluded_url(url: str, exclude_url_patterns: list[str]) -> bool:
    return _is_excluded_url(url=url, exclude_url_patterns=exclude_url_patterns)


def _is_excluded_crawled_page(crawled_page: CrawledPage, product: str, exclude_url_patterns: list[str]) -> bool:
    if crawled_page.document.metadata.get("product") != product:
        return True
    if _is_excluded_url(crawled_page.document.url, exclude_url_patterns):
        return True
    document_path = Path(str(crawled_page.document.metadata.get("document_path", "")))
    return document_path.name.startswith("api-")


def _delete_crawled_page_files(crawled_page: CrawledPage) -> None:
    document_path = Path(str(crawled_page.document.metadata.get("document_path", "")))
    for metadata_key in ("raw_path", "document_path", "metadata_path"):
        path = Path(str(crawled_page.document.metadata.get(metadata_key, "")))
        if path.is_file():
            path.unlink()
            _remove_empty_parents(path.parent, stop_at=document_path.parents[2])


def _remove_empty_parents(path: Path, stop_at: Path) -> None:
    while path != stop_at and stop_at in path.parents:
        try:
            path.rmdir()
        except OSError:
            return
        path = path.parent


def _discover_product_urls(repo_root: Path, product: str) -> list[str]:
    known_urls = {document["url"] for document in _manifest_documents(repo_root) if "url" in document}
    documents_dir = repo_root / "data" / "datasources" / "aliyun-docs" / "products" / product / "documents"
    if not documents_dir.exists():
        return []

    urls: list[str] = []
    seen_urls: set[str] = set()
    pattern = re.compile(rf"products/{re.escape(product)}/documents/([^)]+)\.md")
    for document_path in sorted(documents_dir.rglob("*.md")):
        markdown = document_path.read_text(encoding="utf-8")
        for match in pattern.finditer(markdown):
            url = _document_link_to_url(product=product, document_link=match.group(1))
            if url not in known_urls and url not in seen_urls:
                seen_urls.add(url)
                urls.append(url)
    return urls


def _document_link_to_url(product: str, document_link: str) -> str:
    if document_link == "index":
        return f"https://help.aliyun.com/zh/{product}/"
    return f"https://help.aliyun.com/zh/{product}/{document_link}"


def _manifest_documents(repo_root: Path) -> list[dict[str, str]]:
    manifest_path = repo_root / "data" / "datasources" / "aliyun-docs" / "manifest.json"
    if not manifest_path.exists():
        return []
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    documents = manifest.get("documents")
    if not isinstance(documents, list):
        return []

    manifest_documents: list[dict[str, str]] = []
    for document in cast(list[object], documents):
        if not isinstance(document, dict):
            continue
        document_data = cast(dict[object, object], document)
        manifest_documents.append({str(key): str(value) for key, value in document_data.items()})
    return manifest_documents


def _sync_manifest_from_metadata(repo_root: Path, crawler: AliyunDocsCrawler) -> None:
    documents = _metadata_documents(repo_root)
    if documents:
        crawler.write_manifest(documents)


def _metadata_documents(repo_root: Path) -> list[RawDocument]:
    data_root = repo_root / "data" / "datasources" / "aliyun-docs"
    products_root = data_root / "products"
    if not products_root.exists():
        return []

    documents: list[RawDocument] = []
    for metadata_path in sorted(products_root.glob("*/metadata/**/*.json")):
        metadata = cast(dict[str, Any], json.loads(metadata_path.read_text(encoding="utf-8")))
        product = str(metadata.get("product", "general"))
        document_path = str(metadata.get("document_path", ""))
        url = str(metadata.get("url", ""))
        title = str(metadata.get("title", url))
        if not document_path or not url:
            continue
        document_metadata: dict[str, str] = {
            "product": product,
            "topic": str(metadata.get("topic", "features")),
            "raw_path": str(metadata.get("raw_path", "")),
            "document_path": document_path,
            "metadata_path": str(metadata_path),
        }
        documents.append(
            RawDocument(
                id=_document_id_from_path(data_root=data_root, product=product, document_path=Path(document_path)),
                source="aliyun_docs",
                url=url,
                title=title,
                content="",
                fetched_at=datetime.now(UTC),
                metadata=document_metadata,
            )
        )
    return documents


def _document_id_from_path(data_root: Path, product: str, document_path: Path) -> str:
    relative_path = document_path.relative_to(data_root / "products" / product / "documents")
    return f"{product}:{relative_path.with_suffix('').as_posix()}"


def _anti_bot_manifest_urls(repo_root: Path, product: str) -> list[str]:
    urls: list[str] = []
    for document in _manifest_documents(repo_root):
        if document.get("product") != product or "url" not in document:
            continue
        if _is_anti_bot_manifest_document(document):
            urls.append(document["url"])
    return urls


def _is_anti_bot_manifest_document(document: dict[str, str]) -> bool:
    raw_path_value = document.get("raw_path")
    if not raw_path_value:
        return False
    raw_path = Path(raw_path_value)
    if not raw_path.exists():
        return False
    return is_aliyun_anti_bot_page(raw_path.read_text(encoding="utf-8", errors="ignore"))


def _write_crawl_report(repo_root: Path, reports: list[ProductCrawlReport]) -> None:
    report_path = repo_root / "data" / "datasources" / "aliyun-docs" / "crawl-report.json"
    retry_path = repo_root / "data" / "datasources" / "aliyun-docs" / "retry-urls.json"
    all_retry_urls = [
        {"product": report.product, "url": url} for report in reports for url in report.remaining_retry_urls
    ]
    summary = Counter[str]()
    for product_report in reports:
        summary["crawled"] += product_report.crawled
        summary["anti_bot"] += product_report.anti_bot
        summary["failed"] += product_report.failed
        summary["retried"] += product_report.retried
        summary["remaining_retry_urls"] += len(product_report.remaining_retry_urls)
    crawl_report: dict[str, Any] = {
        "source": "aliyun_docs",
        "updated_at": datetime.now(UTC).isoformat(),
        "summary": dict(summary),
        "products": [asdict(product_report) for product_report in reports],
    }
    retry_payload: dict[str, Any] = {"source": "aliyun_docs", "urls": all_retry_urls}
    report_path.write_text(json.dumps(crawl_report, ensure_ascii=False, indent=2), encoding="utf-8")
    retry_path.write_text(json.dumps(retry_payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _sleep(seconds: float) -> None:
    if seconds > 0:
        time.sleep(seconds)


if __name__ == "__main__":
    main()
