import json
from collections import deque
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, cast
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen

from knowledge_platform.crawlers.base import CrawlPlan, CrawlRequest, DocumentCrawler
from knowledge_platform.documents.models import RawDocument

ANTI_BOT_MARKERS = ("_____tmd_____", "/punish", "x5secdata")


class AliyunAntiBotPageError(RuntimeError):
    def __init__(self, url: str) -> None:
        super().__init__(f"Aliyun anti-bot page returned for {url}")
        self.url = url


@dataclass(frozen=True)
class FetchResult:
    final_url: str
    status_code: int
    content_type: str
    body: bytes


@dataclass(frozen=True)
class LocalDocumentPaths:
    product: str
    raw_path: Path
    document_path: Path
    metadata_path: Path


@dataclass(frozen=True)
class CrawledPage:
    document: RawDocument
    links: list[str]


class ParsedHtml(HTMLParser):
    def __init__(self, base_url: str, local_link_mapper: Callable[[str], str]) -> None:
        super().__init__()
        self._base_url = base_url
        self._local_link_mapper = local_link_mapper
        self.title = ""
        self.links: list[str] = []
        self.text_parts: list[str] = []
        self.markdown_parts: list[str] = []
        self._in_title = False
        self._ignored_tag_depth = 0
        self._link_href: str | None = None
        self._in_table = False
        self._in_table_cell = False
        self._current_row: list[str] = []
        self._current_cell_parts: list[str] = []
        self._table_rows: list[list[str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized_tag = tag.lower()
        if normalized_tag == "title":
            self._in_title = True
            return
        if normalized_tag in {"script", "style", "noscript"}:
            self._ignored_tag_depth += 1
            return
        if normalized_tag == "a":
            href = self._find_attr(attrs, "href")
            if href:
                self.links.append(href)
                self._link_href = href
            return
        if normalized_tag in {"p", "div", "section", "article", "br"}:
            self._append_markdown_break()
            return
        if normalized_tag in {"h1", "h2", "h3"}:
            self._append_markdown_break()
            self.markdown_parts.append(f"{'#' * int(normalized_tag[1])} ")
            return
        if normalized_tag in {"li"}:
            self._append_markdown_break()
            self.markdown_parts.append("- ")
            return
        if normalized_tag == "table":
            self._in_table = True
            self._table_rows = []
            return
        if normalized_tag == "tr" and self._in_table:
            self._current_row = []
            return
        if normalized_tag in {"td", "th"} and self._in_table:
            self._in_table_cell = True
            self._current_cell_parts = []

    def handle_endtag(self, tag: str) -> None:
        normalized_tag = tag.lower()
        if normalized_tag == "title":
            self._in_title = False
            return
        if normalized_tag in {"script", "style", "noscript"} and self._ignored_tag_depth > 0:
            self._ignored_tag_depth -= 1
            return
        if normalized_tag == "a":
            self._link_href = None
            return
        if normalized_tag in {"h1", "h2", "h3", "p", "div", "section", "article", "li"}:
            self._append_markdown_break()
            return
        if normalized_tag in {"td", "th"} and self._in_table_cell:
            self._current_row.append(" ".join(" ".join(self._current_cell_parts).split()))
            self._current_cell_parts = []
            self._in_table_cell = False
            return
        if normalized_tag == "tr" and self._in_table and self._current_row:
            self._table_rows.append(self._current_row)
            self._current_row = []
            return
        if normalized_tag == "table" and self._in_table:
            self._append_markdown_table()
            self._table_rows = []
            self._in_table = False

    def handle_data(self, data: str) -> None:
        normalized_data = " ".join(data.split())
        if not normalized_data:
            return
        if self._in_title:
            self.title = normalized_data if not self.title else f"{self.title} {normalized_data}"
            return
        if self._ignored_tag_depth == 0:
            self.text_parts.append(normalized_data)
            markdown_text = self._format_markdown_text(normalized_data)
            if self._in_table_cell:
                self._current_cell_parts.append(markdown_text)
            elif not self._in_table:
                self.markdown_parts.append(markdown_text)

    def _find_attr(self, attrs: list[tuple[str, str | None]], name: str) -> str | None:
        for attr_name, attr_value in attrs:
            if attr_name.lower() == name and attr_value:
                return attr_value
        return None

    def _format_markdown_text(self, text: str) -> str:
        if not self._link_href:
            return text
        absolute_url = urljoin(self._base_url, self._link_href)
        return f"[{text}]({self._local_link_mapper(absolute_url)})"

    def _append_markdown_break(self) -> None:
        if self.markdown_parts and self.markdown_parts[-1] != "\n\n":
            self.markdown_parts.append("\n\n")

    def _append_markdown_table(self) -> None:
        if not self._table_rows:
            return
        width = max(len(row) for row in self._table_rows)
        rows = [row + [""] * (width - len(row)) for row in self._table_rows]
        self._append_markdown_break()
        self.markdown_parts.append("| " + " | ".join(rows[0]) + " |\n")
        self.markdown_parts.append("| " + " | ".join("---" for _ in range(width)) + " |\n")
        for row in rows[1:]:
            self.markdown_parts.append("| " + " | ".join(row) + " |\n")
        self._append_markdown_break()


class AliyunDocsCrawler(DocumentCrawler):
    source = "aliyun_docs"
    data_source_dir = "aliyun-docs"
    allowed_domains = ["help.aliyun.com", "www.alibabacloud.com"]
    product_slugs = {
        "ack",
        "apsaramq-for-rocketmq",
        "arms",
        "cdn",
        "cen",
        "cloudmonitor",
        "ecs",
        "eip",
        "fc",
        "kms",
        "model-studio",
        "nat-gateway",
        "oss",
        "rds",
        "redis",
        "rocketmq",
        "ram",
        "slb",
        "sls",
        "vpc",
        "vpn-gateway",
        "waf",
    }
    product_aliases = {
        "apsaramq-for-rocketmq": "rocketmq",
    }

    def __init__(
        self,
        data_root: Path | None = None,
        fetcher: Callable[[str], FetchResult] | None = None,
    ) -> None:
        self._data_root = data_root or self._default_data_root()
        self._fetcher = fetcher or self._fetch_url

    def build_plan(self, request: CrawlRequest) -> CrawlPlan:
        unsupported_urls = [url for url in request.seed_urls if self._normalize_domain(url) not in self.allowed_domains]
        if unsupported_urls:
            unsupported_text = ", ".join(unsupported_urls)
            raise ValueError(f"Unsupported Aliyun docs URL: {unsupported_text}")

        return CrawlPlan(
            source=self.source,
            seed_urls=request.seed_urls,
            allowed_domains=self.allowed_domains,
            max_pages=request.max_pages,
            max_depth=request.max_depth,
        )

    def crawl(self, request: CrawlRequest) -> list[RawDocument]:
        self.build_plan(request)

        documents: list[RawDocument] = []
        visited_urls: set[str] = set()
        seed_products = {self._product_from_url(seed_url) for seed_url in request.seed_urls}
        pending_urls: deque[tuple[str, int]] = deque(
            (self._normalize_url(seed_url), 0) for seed_url in request.seed_urls
        )

        while pending_urls and len(documents) < request.max_pages:
            current_url, depth = pending_urls.popleft()
            if current_url in visited_urls:
                continue
            visited_urls.add(current_url)

            try:
                crawled_page = self.crawl_page(current_url)
                if crawled_page is None:
                    continue
            except AliyunAntiBotPageError:
                continue

            documents.append(crawled_page.document)

            if depth >= request.max_depth:
                continue
            for next_url in crawled_page.links:
                next_product = self._product_from_url(next_url)
                if (
                    self._normalize_domain(next_url) in self.allowed_domains
                    and next_product in seed_products
                    and next_url not in visited_urls
                ):
                    pending_urls.append((next_url, depth + 1))

        self.write_manifest(documents)
        return documents

    def crawl_page(self, url: str) -> CrawledPage | None:
        fetch_result = self._fetcher(url)
        if fetch_result.status_code < 200 or fetch_result.status_code >= 300:
            raise RuntimeError(f"Failed to fetch {url}: HTTP {fetch_result.status_code}")
        if "html" not in fetch_result.content_type.lower():
            return None

        html = self._decode_body(fetch_result.body, fetch_result.content_type)
        if is_aliyun_anti_bot_page(html):
            raise AliyunAntiBotPageError(fetch_result.final_url)

        parsed_html = self._parse_html(html, fetch_result.final_url)
        fetched_at = datetime.now(UTC)
        local_paths = self._build_local_paths(fetch_result.final_url)
        document_id = self._document_id(local_paths.product, fetch_result.final_url)
        title = parsed_html.title or fetch_result.final_url
        topic = self._infer_topic(fetch_result.final_url, title)
        content = "\n".join(parsed_html.text_parts)
        markdown = self._build_markdown(title=title, url=fetch_result.final_url, parsed_html=parsed_html)

        self._write_text_file(local_paths.raw_path, html)
        self._write_text_file(local_paths.document_path, markdown)
        page_metadata: dict[str, Any] = {
            "source": self.source,
            "product": local_paths.product,
            "topic": topic,
            "url": fetch_result.final_url,
            "title": title,
            "fetched_at": fetched_at.isoformat(),
            "status_code": str(fetch_result.status_code),
            "content_type": fetch_result.content_type,
            "raw_path": str(local_paths.raw_path),
            "document_path": str(local_paths.document_path),
        }
        self._write_json_file(
            local_paths.metadata_path,
            metadata=page_metadata,
        )

        document_metadata: dict[str, str] = {
            "product": local_paths.product,
            "topic": topic,
            "content_type": fetch_result.content_type,
            "raw_path": str(local_paths.raw_path),
            "document_path": str(local_paths.document_path),
            "metadata_path": str(local_paths.metadata_path),
        }
        document = RawDocument(
            id=document_id,
            source=self.source,
            url=fetch_result.final_url,
            title=title,
            content=content,
            fetched_at=fetched_at,
            metadata=document_metadata,
        )
        links = [self._normalize_url(urljoin(fetch_result.final_url, link)) for link in parsed_html.links]
        return CrawledPage(document=document, links=links)

    def product_from_url(self, url: str) -> str:
        return self._product_from_url(url)

    def is_allowed_product_url(self, url: str, product: str) -> bool:
        return self._normalize_domain(url) in self.allowed_domains and self._product_from_url(url) == product

    def _normalize_domain(self, url: str) -> str:
        parsed_url = urlparse(url)
        return parsed_url.netloc.lower()

    def _normalize_url(self, url: str) -> str:
        normalized_url, _fragment = urldefrag(url)
        return normalized_url

    def _parse_html(self, html: str, base_url: str) -> ParsedHtml:
        parser = ParsedHtml(base_url=base_url, local_link_mapper=self._local_markdown_link)
        parser.feed(html)
        return parser

    def _decode_body(self, body: bytes, content_type: str) -> str:
        charset = "utf-8"
        for part in content_type.split(";"):
            normalized_part = part.strip().lower()
            if normalized_part.startswith("charset="):
                charset = normalized_part.removeprefix("charset=")
                break
        return body.decode(charset, errors="replace")

    def _fetch_url(self, url: str) -> FetchResult:
        request = Request(
            url,
            headers={"User-Agent": "knowledge-platform-aliyun-docs-crawler/0.1"},
        )
        try:
            with urlopen(request, timeout=10) as response:
                return FetchResult(
                    final_url=response.url,
                    status_code=response.status,
                    content_type=response.headers.get("Content-Type", ""),
                    body=response.read(),
                )
        except HTTPError as exc:
            return FetchResult(
                final_url=url,
                status_code=exc.code,
                content_type=exc.headers.get("Content-Type", ""),
                body=exc.read(),
            )
        except URLError as exc:
            raise RuntimeError(f"Failed to fetch {url}: {exc.reason}") from exc

    def _build_markdown(self, title: str, url: str, parsed_html: ParsedHtml) -> str:
        markdown_body = "".join(parsed_html.markdown_parts)
        return f"# {title}\n\nSource: {url}\n\n{markdown_body.strip()}\n"

    def _build_local_paths(self, url: str) -> LocalDocumentPaths:
        product = self._product_from_url(url)
        relative_path = self._relative_page_path(url)
        product_root = self._data_root / "datasources" / self.data_source_dir / "products" / product
        return LocalDocumentPaths(
            product=product,
            raw_path=product_root / "raw" / relative_path.with_suffix(".html"),
            document_path=product_root / "documents" / relative_path.with_suffix(".md"),
            metadata_path=product_root / "metadata" / relative_path.with_suffix(".json"),
        )

    def _relative_page_path(self, url: str) -> Path:
        parsed_url = urlparse(url)
        segments = [quote(segment, safe="-_.~") for segment in parsed_url.path.split("/") if segment]
        product = self._product_from_url(url)
        if product in segments:
            product_index = segments.index(product)
            segments = segments[product_index + 1 :]
        if not segments:
            return Path("index")
        if "." in segments[-1]:
            segments[-1] = segments[-1].rsplit(".", maxsplit=1)[0]
        return Path(*segments)

    def _product_from_url(self, url: str) -> str:
        parsed_url = urlparse(url)
        segments = [segment for segment in parsed_url.path.split("/") if segment]
        for segment in segments:
            if segment in self.product_slugs:
                return self.product_aliases.get(segment, segment)
        return "general"

    def _local_markdown_link(self, url: str) -> str:
        if self._normalize_domain(url) not in self.allowed_domains:
            return url
        if self._product_from_url(url) == "general":
            return url
        paths = self._build_local_paths(url)
        return str(paths.document_path.relative_to(self._data_root / "datasources" / self.data_source_dir))

    def _infer_topic(self, url: str, title: str) -> str:
        text = f"{url} {title}".lower()
        if any(keyword in text for keyword in ["price", "pricing", "bill", "计费", "价格", "费用"]):
            return "pricing"
        if any(keyword in text for keyword in ["quickstart", "deploy", "install", "connect", "部署", "开通", "连接"]):
            return "deployment"
        if any(keyword in text for keyword in ["spec", "performance", "limit", "规格", "性能", "限制"]):
            return "performance"
        if any(keyword in text for keyword in ["troubleshoot", "faq", "error", "问题", "故障", "报错"]):
            return "troubleshoot"
        if any(keyword in text for keyword in ["select", "compare", "scenario", "选型", "对比", "场景"]):
            return "selection"
        return "features"

    def _document_id(self, product: str, url: str) -> str:
        return f"{product}:{self._relative_page_path(url).as_posix()}"

    def _write_text_file(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _write_json_file(self, path: Path, metadata: dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    def write_manifest(self, documents: list[RawDocument]) -> None:
        manifest_path = self._data_root / "datasources" / self.data_source_dir / "manifest.json"
        existing_documents = self._read_manifest_documents(manifest_path)
        document_by_id = {document["id"]: document for document in existing_documents}
        for document in documents:
            document_by_id[document.id] = {
                "id": document.id,
                "product": document.metadata["product"],
                "topic": document.metadata["topic"],
                "url": document.url,
                "title": document.title,
                "raw_path": document.metadata["raw_path"],
                "document_path": document.metadata["document_path"],
                "metadata_path": document.metadata["metadata_path"],
            }
        manifest: dict[str, Any] = {
            "source": self.source,
            "updated_at": datetime.now(UTC).isoformat(),
            "documents": list(document_by_id.values()),
        }
        self._write_json_file(manifest_path, manifest)

    def _read_manifest_documents(self, manifest_path: Path) -> list[dict[str, str]]:
        if not manifest_path.exists():
            return []
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        documents = manifest.get("documents")
        if not isinstance(documents, list):
            return []

        manifest_documents: list[dict[str, str]] = []
        manifest_items = cast(list[object], documents)
        for document in manifest_items:
            if not isinstance(document, dict):
                continue
            raw_document = cast(dict[object, object], document)
            document_data = {str(key): str(value) for key, value in raw_document.items()}
            if "id" in document_data:
                manifest_documents.append(document_data)
        return manifest_documents

    def _default_data_root(self) -> Path:
        return Path(__file__).resolve().parents[4] / "data"


def is_aliyun_anti_bot_page(html: str) -> bool:
    return any(marker in html for marker in ANTI_BOT_MARKERS)
