import json
from pathlib import Path

from knowledge_platform.scripts.index_aliyun_docs import (
    BatchIndexReport,
    estimate_embedding_cost_cny,
    usage_total_from_reports,
    write_index_report,
)


def test_usage_total_sums_batch_usage() -> None:
    reports = [
        BatchIndexReport(
            batch_index=0,
            input_chunks=10,
            skipped_existing=0,
            embedded=10,
            indexed=10,
            request_id="request-1",
            usage={"prompt_tokens": 100, "total_tokens": 100},
        ),
        BatchIndexReport(
            batch_index=1,
            input_chunks=10,
            skipped_existing=2,
            embedded=8,
            indexed=8,
            request_id="request-2",
            usage={"prompt_tokens": 80, "total_tokens": 80},
        ),
    ]

    assert usage_total_from_reports(reports) == {"prompt_tokens": 180, "total_tokens": 180}


def test_estimate_embedding_cost_uses_total_tokens() -> None:
    assert estimate_embedding_cost_cny({"prompt_tokens": 1000, "total_tokens": 2_500_000}, 0.6) == 1.5


def test_write_index_report_includes_usage_and_cost(tmp_path: Path) -> None:
    report_path = tmp_path / "index-report.json"
    reports = [
        BatchIndexReport(
            batch_index=0,
            input_chunks=10,
            skipped_existing=0,
            embedded=10,
            indexed=10,
            request_id="request-1",
            usage={"prompt_tokens": 1_000_000, "total_tokens": 1_000_000},
        )
    ]

    write_index_report(
        report_path=report_path,
        collection="aliyun_docs_product_v1",
        qdrant_endpoint="http://localhost:6333",
        embedding_model="text-embedding-v4",
        source_chunk_count=10,
        indexed=10,
        batch_size=10,
        concurrency=2,
        dry_run=False,
        skip_existing=False,
        embedding_price_per_million_tokens=0.6,
        elapsed_seconds=12.3456,
        reports=reports,
    )

    report = json.loads(report_path.read_text(encoding="utf-8"))

    assert report["usage_total"] == {"prompt_tokens": 1_000_000, "total_tokens": 1_000_000}
    assert report["embedding_price_per_million_tokens"] == 0.6
    assert report["estimated_embedding_cost_cny"] == 0.6
    assert report["elapsed_seconds"] == 12.346
