from knowledge_platform.services.retrieval_service import (
    deduplicate_scored_points,
    evaluate_retrieval_quality,
    product_payload_filter,
)
from knowledge_platform.sessions.models import Citation
from knowledge_platform.vectorstores.qdrant import QdrantConfig, QdrantVectorStore, ScoredVectorPoint


def test_product_payload_filter_matches_product_slug() -> None:
    assert product_payload_filter("ecs") == {
        "must": [
            {
                "key": "product",
                "match": {"value": "ecs"},
            }
        ]
    }


def test_product_payload_filter_is_none_without_product() -> None:
    assert product_payload_filter(None) is None
    assert product_payload_filter("") is None


def test_deduplicate_scored_points_by_source_url() -> None:
    results = [
        ScoredVectorPoint(id="1", score=0.9, payload={"source_url": "https://example.com/a"}),
        ScoredVectorPoint(id="2", score=0.8, payload={"source_url": "https://example.com/a"}),
        ScoredVectorPoint(id="3", score=0.7, payload={"source_url": "https://example.com/b"}),
    ]

    deduplicated = deduplicate_scored_points(results, limit=2)

    assert [result.id for result in deduplicated] == ["1", "3"]


def test_evaluate_retrieval_quality_counts_product_matches() -> None:
    quality = evaluate_retrieval_quality(
        citations=[
            Citation(
                title="ECS overview",
                url="https://help.aliyun.com/zh/ecs/product-overview",
                source="aliyun_docs",
                score=0.8,
            )
        ],
        product_filter="ecs",
    )

    assert quality.target_product_citations == 1
    assert quality.off_product_citations == 0
    assert quality.interface_reference_citations == 0
    assert quality.top_score == 0.8
    assert quality.avg_score == 0.8
    assert quality.quality_warnings == []


def test_evaluate_retrieval_quality_warns_for_off_product_interface_reference() -> None:
    quality = evaluate_retrieval_quality(
        citations=[
            Citation(
                title="API参考",
                url="https://help.aliyun.com/zh/rds/developer-reference/api-create",
                source="aliyun_docs",
                score=0.4,
            )
        ],
        product_filter="ecs",
    )

    assert quality.target_product_citations == 0
    assert quality.off_product_citations == 1
    assert quality.interface_reference_citations == 1
    assert quality.quality_warnings == ["off_product_citations", "interface_reference_citations", "low_top_score"]


def test_qdrant_ensure_collection_ignores_existing_collection() -> None:
    class ExistingCollectionVectorStore(QdrantVectorStore):
        def _request_json(self, method: str, path: str, payload: dict[str, object]) -> dict[str, object]:
            raise RuntimeError("Qdrant request failed: HTTP 409: Collection `demo` already exists!")

        def ensure_sync_for_test(self) -> None:
            self._ensure_collection_sync(vector_size=10)

    ExistingCollectionVectorStore(config=QdrantConfig()).ensure_sync_for_test()
