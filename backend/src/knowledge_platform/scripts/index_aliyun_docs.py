import argparse
import asyncio
import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, cast

from knowledge_platform.embeddings.dashscope import (
    DEFAULT_DASHSCOPE_EMBEDDING_MODEL,
    DashScopeEmbeddingProvider,
    dashscope_config_from_env,
)
from knowledge_platform.vectorstores.qdrant import QdrantConfig, QdrantVectorStore, vector_point_from_record


@dataclass
class CollectionState:
    vector_size: int | None = None


@dataclass(frozen=True)
class BatchIndexReport:
    batch_index: int
    input_chunks: int
    skipped_existing: int
    embedded: int
    indexed: int
    request_id: str
    usage: dict[str, int]


@dataclass(frozen=True)
class IndexResult:
    indexed: int
    report: BatchIndexReport


def main() -> None:
    asyncio.run(_main_async())


async def _main_async() -> None:
    args = _parse_args()
    repo_root = Path(__file__).resolve().parents[4]
    data_root = repo_root / "data" / "datasources" / "aliyun-docs"
    manifest_path = data_root / "chunk-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    records = _read_chunk_records(manifest)
    if args.limit is not None:
        records = records[: args.limit]
    if args.max_batches is not None:
        records = records[: args.max_batches * args.batch_size]

    embedding_config = dashscope_config_from_env()
    provider = DashScopeEmbeddingProvider(config=embedding_config)
    vector_store = QdrantVectorStore(
        config=QdrantConfig(
            endpoint=args.qdrant_endpoint,
            collection_name=args.collection,
            timeout_seconds=args.qdrant_timeout_seconds,
        )
    )
    collection_state = CollectionState()
    collection_lock = asyncio.Lock()

    total_indexed = 0
    reports: list[BatchIndexReport] = []
    batches = list(_batches(records, args.batch_size))
    semaphore = asyncio.Semaphore(args.concurrency)
    tasks = [
        _index_batch(
            batch_index=batch_index,
            batch=batch,
            provider=provider,
            vector_store=vector_store,
            collection_state=collection_state,
            collection_lock=collection_lock,
            semaphore=semaphore,
            dry_run=args.dry_run,
            skip_existing=not args.no_skip_existing,
        )
        for batch_index, batch in enumerate(batches)
    ]
    for task in asyncio.as_completed(tasks):
        result = await task
        total_indexed += result.indexed
        reports.append(result.report)

    reports.sort(key=lambda report: report.batch_index)
    report_path = _report_path(data_root=data_root, value=args.report_path)
    _write_index_report(
        report_path=report_path,
        collection=args.collection,
        qdrant_endpoint=args.qdrant_endpoint,
        embedding_model=embedding_config.model,
        source_chunk_count=len(records),
        indexed=total_indexed,
        batch_size=args.batch_size,
        concurrency=args.concurrency,
        dry_run=args.dry_run,
        skip_existing=not args.no_skip_existing,
        reports=reports,
    )
    print(f"chunks: {len(records)}")
    print(f"indexed: {total_indexed}")
    print(f"skipped_existing: {sum(report.skipped_existing for report in reports)}")
    print(f"collection: {args.collection}")
    print(f"report: {report_path}")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Index Aliyun documentation chunks into Qdrant.")
    parser.add_argument("--collection", default="aliyun_docs_product_v1", help="Qdrant collection name.")
    parser.add_argument("--qdrant-endpoint", default="http://localhost:6333", help="Qdrant HTTP endpoint.")
    parser.add_argument("--qdrant-timeout-seconds", type=float, default=30.0, help="Qdrant request timeout.")
    parser.add_argument("--batch-size", type=int, default=10, help="Embedding and upsert batch size.")
    parser.add_argument("--concurrency", type=int, default=2, help="Concurrent embedding/upsert batches.")
    parser.add_argument("--limit", type=int, default=None, help="Optional maximum chunks to index.")
    parser.add_argument("--max-batches", type=int, default=None, help="Optional maximum batches to index.")
    parser.add_argument(
        "--report-path",
        default=None,
        help="Index report path. Defaults to data source index-report.json.",
    )
    parser.add_argument("--no-skip-existing", action="store_true", help="Re-embed chunks even if points already exist.")
    parser.add_argument("--dry-run", action="store_true", help="Read chunks without embedding or upserting.")
    return parser.parse_args()


async def _index_batch(
    batch_index: int,
    batch: list[dict[str, Any]],
    provider: DashScopeEmbeddingProvider,
    vector_store: QdrantVectorStore,
    collection_state: CollectionState,
    collection_lock: asyncio.Lock,
    semaphore: asyncio.Semaphore,
    dry_run: bool,
    skip_existing: bool,
) -> IndexResult:
    async with semaphore:
        records_to_index = batch
        skipped_existing = 0
        if skip_existing and not dry_run:
            existing_source_ids = await vector_store.existing_source_ids([str(record["id"]) for record in batch])
            records_to_index = [record for record in batch if str(record["id"]) not in existing_source_ids]
            skipped_existing = len(batch) - len(records_to_index)

        chunk_contents = await asyncio.gather(*[_read_chunk_content(record) for record in records_to_index])
        if dry_run:
            return IndexResult(
                indexed=len(chunk_contents),
                report=BatchIndexReport(
                    batch_index=batch_index,
                    input_chunks=len(batch),
                    skipped_existing=0,
                    embedded=0,
                    indexed=len(chunk_contents),
                    request_id="",
                    usage={},
                ),
            )
        if not records_to_index:
            return IndexResult(
                indexed=0,
                report=BatchIndexReport(
                    batch_index=batch_index,
                    input_chunks=len(batch),
                    skipped_existing=skipped_existing,
                    embedded=0,
                    indexed=0,
                    request_id="",
                    usage={},
                ),
            )

        embedding_batch = await provider.embed_texts_with_metadata(chunk_contents)
        embeddings = embedding_batch.embeddings
        if not embeddings:
            return IndexResult(
                indexed=0,
                report=BatchIndexReport(
                    batch_index=batch_index,
                    input_chunks=len(batch),
                    skipped_existing=skipped_existing,
                    embedded=0,
                    indexed=0,
                    request_id=embedding_batch.request_id,
                    usage=embedding_batch.usage,
                ),
            )

        vector_size = len(embeddings[0].vector)
        await _ensure_collection_once(
            vector_store=vector_store,
            collection_state=collection_state,
            collection_lock=collection_lock,
            vector_size=vector_size,
        )
        points = [
            vector_point_from_record(
                record=_record_with_content_hash(
                    record=records_to_index[embedding.text_index],
                    content=chunk_contents[embedding.text_index],
                ),
                vector=embedding.vector,
                content=chunk_contents[embedding.text_index],
            )
            for embedding in embeddings
        ]
        indexed = await vector_store.upsert_points(points)
        return IndexResult(
            indexed=indexed,
            report=BatchIndexReport(
                batch_index=batch_index,
                input_chunks=len(batch),
                skipped_existing=skipped_existing,
                embedded=len(embeddings),
                indexed=indexed,
                request_id=embedding_batch.request_id,
                usage=embedding_batch.usage,
            ),
        )


async def _ensure_collection_once(
    vector_store: QdrantVectorStore,
    collection_state: CollectionState,
    collection_lock: asyncio.Lock,
    vector_size: int,
) -> None:
    async with collection_lock:
        if collection_state.vector_size is None:
            await vector_store.ensure_collection(vector_size=vector_size)
            collection_state.vector_size = vector_size
            return
        if collection_state.vector_size != vector_size:
            raise RuntimeError(
                f"embedding vector size changed from {collection_state.vector_size} to {vector_size}"
            )


async def _read_chunk_content(record: dict[str, Any]) -> str:
    chunk_path = Path(str(record["chunk_path"]))
    return await asyncio.to_thread(chunk_path.read_text, encoding="utf-8")


def _read_chunk_records(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    chunks = manifest.get("chunks")
    if not isinstance(chunks, list):
        return []
    records: list[dict[str, Any]] = []
    for chunk in cast(list[object], chunks):
        if isinstance(chunk, dict):
            records.append(cast(dict[str, Any], chunk))
    return records


def _batches(records: list[dict[str, Any]], batch_size: int) -> list[list[dict[str, Any]]]:
    if batch_size <= 0:
        raise ValueError("batch_size must be greater than 0")
    return [records[index : index + batch_size] for index in range(0, len(records), batch_size)]


def _record_with_content_hash(record: dict[str, Any], content: str) -> dict[str, Any]:
    updated_record = dict(record)
    updated_record["content_sha256"] = hashlib.sha256(content.encode("utf-8")).hexdigest()
    return updated_record


def _report_path(data_root: Path, value: str | None) -> Path:
    if not value:
        return data_root / "index-report.json"
    return Path(value)


def _write_index_report(
    report_path: Path,
    collection: str,
    qdrant_endpoint: str,
    embedding_model: str,
    source_chunk_count: int,
    indexed: int,
    batch_size: int,
    concurrency: int,
    dry_run: bool,
    skip_existing: bool,
    reports: list[BatchIndexReport],
) -> None:
    report = {
        "source": "aliyun_docs",
        "updated_at": datetime.now(UTC).isoformat(),
        "collection": collection,
        "qdrant_endpoint": qdrant_endpoint,
        "embedding_model": embedding_model or DEFAULT_DASHSCOPE_EMBEDDING_MODEL,
        "source_chunk_count": source_chunk_count,
        "indexed": indexed,
        "skipped_existing": sum(batch_report.skipped_existing for batch_report in reports),
        "batch_size": batch_size,
        "concurrency": concurrency,
        "dry_run": dry_run,
        "skip_existing": skip_existing,
        "batches": [asdict(batch_report) for batch_report in reports],
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
