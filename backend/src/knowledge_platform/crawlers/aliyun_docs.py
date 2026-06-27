import json
from collections import deque
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen

from knowledge_platform.crawlers.base import CrawlPlan, CrawlRequest, DocumentCrawler
from knowledge_platform.documents.models import RawDocument


@dataclass(frozen=True)
class FetchResult:
    final_url: str
    status_code: int
    content_type: str
    body: bytes


class ParsedHtml(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.links: list[str] = []
        self.text_parts: list[str] = []
        self._in_title = False
        self._ignored_tag_depth = 0

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

    def handle_endtag(self, tag: str) -> None:
        normalized_tag = tag.lower()
        if normalized_tag == "title":
            self._in_title = False
            return
        if normalized_tag in {"script", "style", "noscript"} and self._ignored_tag_depth > 0:
            self._ignored_tag_depth -= 1

    def handle_data(self, data: str) -> None:
        normalized_data = " ".join(data.split())
        if not normalized_data:
            return
        if self._in_title:
            self.title = normalized_data if not self.title else f"{self.title} {normalized_data}"
            return
        if self._ignored_tag_depth == 0:
            self.text_parts.append(normalized_data)

    def _find_attr(self, attrs: list[tuple[str, str | None]], name: str) -> str | None:
        for attr_name, attr_value in attrs:
            if attr_name.lower() == name and attr_value:
                return attr_value
        return None


class AliyunDocsCrawler(DocumentCrawler):
    source = "aliyun_docs"
    data_source_dir = "aliyun-docs"
    allowed_domains = ["help.aliyun.com", "www.alibabacloud.com"]

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
        pending_urls: deque[tuple[str, int]] = deque(
            (self._normalize_url(seed_url), 0) for seed_url in request.seed_urls
        )

        while pending_urls and len(documents) < request.max_pages:
            current_url, depth = pending_urls.popleft()
            if current_url in visited_urls:
                continue
            visited_urls.add(current_url)

            fetch_result = self._fetcher(current_url)
            if fetch_result.status_code < 200 or fetch_result.status_code >= 300:
                raise RuntimeError(f"Failed to fetch {current_url}: HTTP {fetch_result.status_code}")
            if "html" not in fetch_result.content_type.lower():
                continue

            html = self._decode_body(fetch_result.body, fetch_result.content_type)
            parsed_html = self._parse_html(html)
            fetched_at = datetime.now(UTC)
            document_id = self._url_hash(fetch_result.final_url)
            title = parsed_html.title or fetch_result.final_url
            content = "\n".join(parsed_html.text_parts)

            raw_path = self._write_raw_html(document_id=document_id, html=html)
            metadata_path = self._write_metadata(
                document_id=document_id,
                metadata={
                    "source": self.source,
                    "url": fetch_result.final_url,
                    "title": title,
                    "fetched_at": fetched_at.isoformat(),
                    "status_code": str(fetch_result.status_code),
                    "content_type": fetch_result.content_type,
                    "raw_path": str(raw_path),
                },
            )

            documents.append(
                RawDocument(
                    id=document_id,
                    source=self.source,
                    url=fetch_result.final_url,
                    title=title,
                    content=content,
                    fetched_at=fetched_at,
                    metadata={
                        "content_type": fetch_result.content_type,
                        "raw_path": str(raw_path),
                        "metadata_path": str(metadata_path),
                    },
                )
            )

            if depth >= request.max_depth:
                continue
            for link in parsed_html.links:
                next_url = self._normalize_url(urljoin(fetch_result.final_url, link))
                if self._normalize_domain(next_url) in self.allowed_domains and next_url not in visited_urls:
                    pending_urls.append((next_url, depth + 1))

        return documents

    def _normalize_domain(self, url: str) -> str:
        parsed_url = urlparse(url)
        return parsed_url.netloc.lower()

    def _normalize_url(self, url: str) -> str:
        normalized_url, _fragment = urldefrag(url)
        return normalized_url

    def _parse_html(self, html: str) -> ParsedHtml:
        parser = ParsedHtml()
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

    def _write_raw_html(self, document_id: str, html: str) -> Path:
        raw_dir = self._data_root / "datasources" / self.data_source_dir / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)
        raw_path = raw_dir / f"{document_id}.html"
        raw_path.write_text(html, encoding="utf-8")
        return raw_path

    def _write_metadata(self, document_id: str, metadata: dict[str, str]) -> Path:
        metadata_dir = self._data_root / "datasources" / self.data_source_dir / "metadata"
        metadata_dir.mkdir(parents=True, exist_ok=True)
        metadata_path = metadata_dir / f"{document_id}.json"
        metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
        return metadata_path

    def _url_hash(self, url: str) -> str:
        return sha256(url.encode("utf-8")).hexdigest()[:16]

    def _default_data_root(self) -> Path:
        return Path(__file__).resolve().parents[4] / "data"
