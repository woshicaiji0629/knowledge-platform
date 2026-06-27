import json
from pathlib import Path

from knowledge_platform.crawlers.aliyun_docs import AliyunDocsCrawler, FetchResult
from knowledge_platform.crawlers.base import CrawlRequest


def test_aliyun_docs_crawler_saves_raw_html_and_metadata(tmp_path: Path) -> None:
    pages = {
        "https://help.aliyun.com/start": FetchResult(
            final_url="https://help.aliyun.com/start",
            status_code=200,
            content_type="text/html; charset=utf-8",
            body=(
                b"<html><head><title>Start Page</title></head>"
                b"<body><main>Start content</main><a href='/next'>Next</a></body></html>"
            ),
        ),
        "https://help.aliyun.com/next": FetchResult(
            final_url="https://help.aliyun.com/next",
            status_code=200,
            content_type="text/html; charset=utf-8",
            body=b"<html><head><title>Next Page</title></head><body>Next content</body></html>",
        ),
    }

    def fetcher(url: str) -> FetchResult:
        return pages[url]

    crawler = AliyunDocsCrawler(data_root=tmp_path, fetcher=fetcher)

    documents = crawler.crawl(CrawlRequest(seed_urls=["https://help.aliyun.com/start"], max_pages=2, max_depth=1))

    assert [document.title for document in documents] == ["Start Page", "Next Page"]
    assert "Start content" in documents[0].content
    assert documents[1].content == "Next content"

    raw_path = Path(documents[0].metadata["raw_path"])
    metadata_path = Path(documents[0].metadata["metadata_path"])

    assert raw_path.is_file()
    assert metadata_path.is_file()
    assert raw_path.parent == tmp_path / "datasources" / "aliyun-docs" / "raw"
    assert metadata_path.parent == tmp_path / "datasources" / "aliyun-docs" / "metadata"
    assert "Start content" in raw_path.read_text(encoding="utf-8")

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["source"] == "aliyun_docs"
    assert metadata["url"] == "https://help.aliyun.com/start"
    assert metadata["title"] == "Start Page"
    assert metadata["content_type"] == "text/html; charset=utf-8"
    assert metadata["raw_path"] == str(raw_path)


def test_aliyun_docs_crawler_rejects_unsupported_domains(tmp_path: Path) -> None:
    crawler = AliyunDocsCrawler(data_root=tmp_path)

    try:
        crawler.crawl(CrawlRequest(seed_urls=["https://example.com/docs"], max_pages=1, max_depth=0))
    except ValueError as exc:
        assert "Unsupported Aliyun docs URL" in str(exc)
    else:
        raise AssertionError("Expected unsupported domain to raise ValueError")
