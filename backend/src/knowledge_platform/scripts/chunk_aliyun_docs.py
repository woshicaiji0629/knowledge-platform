import argparse
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, cast

from knowledge_platform.documents.chunker import DocumentChunker, create_chunker
from knowledge_platform.documents.models import DocumentChunk, RawDocument


@dataclass(frozen=True)
class ChunkRecord:
    id: str
    document_id: str
    product: str
    topic: str
    title: str
    source_url: str
    chunk_index: int
    chunk_path: str
    metadata_path: str
    char_count: int
    heading_path: str


def main() -> None:
    args = _parse_args()
    repo_root = Path(__file__).resolve().parents[4]
    data_root = repo_root / "data" / "datasources" / "aliyun-docs"
    manifest_path = data_root / "cleaned-manifest.json"
    manifest = cast(dict[str, Any], json.loads(manifest_path.read_text(encoding="utf-8")))
    documents = _read_documents(manifest)

    chunker = create_chunker(
        name=args.chunker,
        max_chars=args.max_chars,
        overlap_chars=args.overlap_chars,
        min_content_chars=args.min_content_chars,
    )
    records = _chunk_documents_concurrently(
        data_root=data_root,
        documents=documents,
        chunker=chunker,
        workers=args.workers,
    )

    _write_chunk_manifest(
        data_root=data_root,
        records=records,
        chunker_name=args.chunker,
        max_chars=args.max_chars,
        overlap_chars=args.overlap_chars,
        min_content_chars=args.min_content_chars,
    )
    print(f"documents: {len(documents)}")
    print(f"chunks: {len(records)}")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Chunk cleaned Aliyun documentation concurrently.")
    parser.add_argument(
        "--chunker",
        default="markdown-heading-table-preserve",
        help="Registered chunker strategy name.",
    )
    parser.add_argument("--max-chars", type=int, default=1200, help="Maximum characters per chunk.")
    parser.add_argument("--overlap-chars", type=int, default=160, help="Overlap characters between chunks.")
    parser.add_argument("--min-content-chars", type=int, default=80, help="Minimum non-heading content characters.")
    parser.add_argument("--workers", type=int, default=_default_workers(), help="Number of concurrent file workers.")
    return parser.parse_args()


def _default_workers() -> int:
    cpu_count = os.cpu_count() or 4
    return max(1, min(cpu_count, 8))


def _chunk_documents_concurrently(
    data_root: Path,
    documents: list[dict[str, str]],
    chunker: DocumentChunker,
    workers: int,
) -> list[ChunkRecord]:
    if workers <= 0:
        raise ValueError("workers must be greater than 0")
    if workers == 1:
        return [
            record
            for document in documents
            for record in _chunk_document(data_root=data_root, document=document, chunker=chunker)
        ]

    records_by_index: dict[int, list[ChunkRecord]] = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(_chunk_document, data_root=data_root, document=document, chunker=chunker): index
            for index, document in enumerate(documents)
        }
        for future in as_completed(futures):
            records_by_index[futures[future]] = future.result()
    return [record for index in range(len(documents)) for record in records_by_index[index]]


def _chunk_document(data_root: Path, document: dict[str, str], chunker: DocumentChunker) -> list[ChunkRecord]:
    raw_document = _to_raw_document(document)
    return [_write_chunk(data_root=data_root, document=document, chunk=chunk) for chunk in chunker.split(raw_document)]


def _to_raw_document(document: dict[str, str]) -> RawDocument:
    document_path = Path(document["cleaned_document_path"])
    content = document_path.read_text(encoding="utf-8")
    document_metadata: dict[str, str] = {
        "product": document["product"],
        "topic": document["topic"],
        "cleaned_document_path": document["cleaned_document_path"],
        "cleaned_metadata_path": document["metadata_path"],
    }
    return RawDocument(
        id=document["id"],
        source="aliyun_docs",
        url=document["source_url"],
        title=document["title"],
        content=content,
        fetched_at=datetime.now(UTC),
        metadata=document_metadata,
    )


def _write_chunk(data_root: Path, document: dict[str, str], chunk: DocumentChunk) -> ChunkRecord:
    chunk_path = _chunk_document_path(
        data_root=data_root, document_path=Path(document["cleaned_document_path"]), chunk=chunk
    )
    metadata_path = _chunk_metadata_path(data_root=data_root, chunk_path=chunk_path)
    chunk_path.parent.mkdir(parents=True, exist_ok=True)
    metadata_path.parent.mkdir(parents=True, exist_ok=True)

    chunk_path.write_text(chunk.content.strip() + "\n", encoding="utf-8")
    metadata: dict[str, Any] = {
        "id": chunk.id,
        "document_id": chunk.document_id,
        "source": chunk.source,
        "product": document["product"],
        "topic": document["topic"],
        "title": chunk.title,
        "source_url": chunk.url,
        "chunk_index": chunk.chunk_index,
        "chunk_path": str(chunk_path),
        "cleaned_document_path": document["cleaned_document_path"],
        "heading_path": chunk.metadata.get("heading_path", ""),
        "char_count": len(chunk.content),
    }
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    return ChunkRecord(
        id=chunk.id,
        document_id=chunk.document_id,
        product=document["product"],
        topic=document["topic"],
        title=chunk.title,
        source_url=chunk.url,
        chunk_index=chunk.chunk_index,
        chunk_path=str(chunk_path),
        metadata_path=str(metadata_path),
        char_count=len(chunk.content),
        heading_path=chunk.metadata.get("heading_path", ""),
    )


def _chunk_document_path(data_root: Path, document_path: Path, chunk: DocumentChunk) -> Path:
    relative_path = document_path.relative_to(data_root / "cleaned" / "products")
    chunk_file = relative_path.with_suffix(f".chunk-{chunk.chunk_index:04d}.md")
    return data_root / "chunks" / "products" / chunk_file


def _chunk_metadata_path(data_root: Path, chunk_path: Path) -> Path:
    relative_path = chunk_path.relative_to(data_root / "chunks" / "products")
    parts = list(relative_path.parts)
    if len(parts) >= 2 and parts[1] == "documents":
        parts[1] = "metadata"
    return data_root / "chunks" / "products" / Path(*parts).with_suffix(".json")


def _write_chunk_manifest(
    data_root: Path,
    records: list[ChunkRecord],
    chunker_name: str,
    max_chars: int,
    overlap_chars: int,
    min_content_chars: int,
) -> None:
    manifest: dict[str, Any] = {
        "source": "aliyun_docs",
        "updated_at": datetime.now(UTC).isoformat(),
        "chunking": {
            "strategy": chunker_name,
            "max_chars": max_chars,
            "overlap_chars": overlap_chars,
            "min_content_chars": min_content_chars,
        },
        "chunk_count": len(records),
        "chunks": [asdict(record) for record in records],
    }
    (data_root / "chunk-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def _read_documents(manifest: dict[str, Any]) -> list[dict[str, str]]:
    documents = manifest.get("documents")
    if not isinstance(documents, list):
        return []
    parsed_documents: list[dict[str, str]] = []
    for document in cast(list[object], documents):
        if not isinstance(document, dict):
            continue
        raw_document = cast(dict[object, object], document)
        parsed_documents.append({str(key): str(value) for key, value in raw_document.items()})
    return parsed_documents


if __name__ == "__main__":
    main()
