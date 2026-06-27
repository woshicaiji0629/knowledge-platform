import json
from pathlib import Path

from knowledge_platform.crawlers.aliyun_docs import AliyunDocsCrawler, FetchResult
from knowledge_platform.crawlers.base import CrawlRequest
from knowledge_platform.scripts.crawl_aliyun_docs import is_excluded_url


def test_aliyun_docs_crawler_saves_raw_html_and_metadata(tmp_path: Path) -> None:
    pages = {
        "https://help.aliyun.com/zh/ecs/": FetchResult(
            final_url="https://help.aliyun.com/zh/ecs/",
            status_code=200,
            content_type="text/html; charset=utf-8",
            body=(
                b"<html><head><title>ECS Start</title></head>"
                b"<body><main>Start content<a href='/zh/ecs/pricing'>Pricing</a>"
                b"<table><tr><th>Name</th><th>Value</th></tr><tr><td>CPU</td><td>2</td></tr></table>"
                b"</main></body></html>"
            ),
        ),
        "https://help.aliyun.com/zh/ecs/pricing": FetchResult(
            final_url="https://help.aliyun.com/zh/ecs/pricing",
            status_code=200,
            content_type="text/html; charset=utf-8",
            body=b"<html><head><title>Pricing Page</title></head><body>Pricing content</body></html>",
        ),
    }

    def fetcher(url: str) -> FetchResult:
        return pages[url]

    crawler = AliyunDocsCrawler(data_root=tmp_path, fetcher=fetcher)

    documents = crawler.crawl(CrawlRequest(seed_urls=["https://help.aliyun.com/zh/ecs/"], max_pages=2, max_depth=1))

    assert [document.title for document in documents] == ["ECS Start", "Pricing Page"]
    assert "Start content" in documents[0].content
    assert documents[1].content == "Pricing content"

    raw_path = Path(documents[0].metadata["raw_path"])
    document_path = Path(documents[0].metadata["document_path"])
    metadata_path = Path(documents[0].metadata["metadata_path"])

    assert raw_path.is_file()
    assert document_path.is_file()
    assert metadata_path.is_file()
    assert raw_path == tmp_path / "datasources" / "aliyun-docs" / "products" / "ecs" / "raw" / "index.html"
    assert document_path == tmp_path / "datasources" / "aliyun-docs" / "products" / "ecs" / "documents" / "index.md"
    assert metadata_path == tmp_path / "datasources" / "aliyun-docs" / "products" / "ecs" / "metadata" / "index.json"
    assert "Start content" in raw_path.read_text(encoding="utf-8")

    markdown = document_path.read_text(encoding="utf-8")
    assert "# ECS Start" in markdown
    assert "[Pricing](products/ecs/documents/pricing.md)" in markdown
    assert "| Name | Value |" in markdown
    assert "| CPU | 2 |" in markdown

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    assert metadata["source"] == "aliyun_docs"
    assert metadata["product"] == "ecs"
    assert metadata["topic"] == "features"
    assert metadata["url"] == "https://help.aliyun.com/zh/ecs/"
    assert metadata["title"] == "ECS Start"
    assert metadata["content_type"] == "text/html; charset=utf-8"
    assert metadata["raw_path"] == str(raw_path)

    manifest_path = tmp_path / "datasources" / "aliyun-docs" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert [document["product"] for document in manifest["documents"]] == ["ecs", "ecs"]


def test_aliyun_docs_crawler_rejects_unsupported_domains(tmp_path: Path) -> None:
    crawler = AliyunDocsCrawler(data_root=tmp_path)

    try:
        crawler.crawl(CrawlRequest(seed_urls=["https://example.com/docs"], max_pages=1, max_depth=0))
    except ValueError as exc:
        assert "Unsupported Aliyun docs URL" in str(exc)
    else:
        raise AssertionError("Expected unsupported domain to raise ValueError")


def test_aliyun_docs_crawler_skips_anti_bot_pages(tmp_path: Path) -> None:
    def fetcher(_url: str) -> FetchResult:
        return FetchResult(
            final_url="https://help.aliyun.com/zh/ecs/",
            status_code=200,
            content_type="text/html; charset=utf-8",
            body=b"<script>window.location.replace('/_____tmd_____/punish?x5secdata=test')</script>",
        )

    crawler = AliyunDocsCrawler(data_root=tmp_path, fetcher=fetcher)

    documents = crawler.crawl(CrawlRequest(seed_urls=["https://help.aliyun.com/zh/ecs/"], max_pages=1, max_depth=0))

    assert documents == []
    manifest_path = tmp_path / "datasources" / "aliyun-docs" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["documents"] == []


def test_crawl_script_excludes_product_api_reference_urls() -> None:
    patterns = ["/developer-reference/api-"]

    assert is_excluded_url("https://help.aliyun.com/zh/vpc/developer-reference/api-vpc-2016-04-28-createvpc", patterns)
    assert not is_excluded_url("https://help.aliyun.com/zh/vpc/developer-reference/endpoint", patterns)
    assert not is_excluded_url("https://help.aliyun.com/zh/vpc/vpc-user-guide/", patterns)
