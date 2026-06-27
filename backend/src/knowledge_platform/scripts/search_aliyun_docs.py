import argparse
import asyncio
import json
from pathlib import Path
from typing import Any

from knowledge_platform.embeddings.dashscope import DashScopeEmbeddingProvider, dashscope_config_from_env
from knowledge_platform.vectorstores.qdrant import QdrantConfig, QdrantVectorStore

DEFAULT_QUERIES = [
    "ECS 怎么选择实例规格？",
    "RDS MySQL 如何备份？",
    "OSS 如何配合 CDN 使用？",
    "Redis 连接数满了怎么办？",
    "ACK 节点池怎么扩容？",
]


def main() -> None:
    asyncio.run(_main_async())


async def _main_async() -> None:
    args = _parse_args()
    queries = args.query or DEFAULT_QUERIES
    provider = DashScopeEmbeddingProvider(config=dashscope_config_from_env())
    vector_store = QdrantVectorStore(
        config=QdrantConfig(
            endpoint=args.qdrant_endpoint,
            collection_name=args.collection,
            timeout_seconds=args.qdrant_timeout_seconds,
        )
    )

    report: list[dict[str, Any]] = []
    for query in queries:
        embedding_batch = await provider.embed_texts_with_metadata([query])
        if not embedding_batch.embeddings:
            continue
        results = await vector_store.search_points(vector=embedding_batch.embeddings[0].vector, limit=args.limit)
        query_report = {
            "query": query,
            "request_id": embedding_batch.request_id,
            "usage": embedding_batch.usage,
            "results": [_result_payload(result.score, result.payload) for result in results],
        }
        report.append(query_report)
        _print_query_report(query_report)

    if args.report_path:
        report_path = Path(args.report_path)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search indexed Aliyun documentation chunks in Qdrant.")
    parser.add_argument("--collection", default="aliyun_docs_product_v1", help="Qdrant collection name.")
    parser.add_argument("--qdrant-endpoint", default="http://localhost:6333", help="Qdrant HTTP endpoint.")
    parser.add_argument("--qdrant-timeout-seconds", type=float, default=30.0, help="Qdrant request timeout.")
    parser.add_argument("--limit", type=int, default=5, help="Search result limit per query.")
    parser.add_argument("--query", action="append", help="Query to search. Can be passed multiple times.")
    parser.add_argument("--report-path", default=None, help="Optional JSON report output path.")
    return parser.parse_args()


def _result_payload(score: float, payload: dict[str, Any]) -> dict[str, Any]:
    content = str(payload.get("content", ""))
    return {
        "score": score,
        "id": str(payload.get("source_id", "")),
        "product": str(payload.get("product", "")),
        "topic": str(payload.get("topic", "")),
        "title": str(payload.get("title", "")),
        "source_url": str(payload.get("source_url", "")),
        "heading_path": str(payload.get("heading_path", "")),
        "chunk_path": str(payload.get("chunk_path", "")),
        "preview": _preview(content),
    }


def _preview(content: str) -> str:
    return " ".join(content.split())[:220]


def _print_query_report(query_report: dict[str, Any]) -> None:
    print(f"\nQUERY: {query_report['query']}")
    for index, result in enumerate(query_report["results"], start=1):
        print(
            f"{index}. score={result['score']:.4f} product={result['product']} "
            f"topic={result['topic']} title={result['title']}"
        )
        if result["heading_path"]:
            print(f"   heading={result['heading_path']}")
        print(f"   url={result['source_url']}")
        print(f"   preview={result['preview']}")


if __name__ == "__main__":
    main()
