import argparse
import json
import os
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

from knowledge_platform.crawlers.aliyun_docs import is_aliyun_anti_bot_page


@dataclass(frozen=True)
class CleanedDocument:
    id: str
    product: str
    topic: str
    title: str
    source_url: str
    raw_document_path: str
    cleaned_document_path: str
    metadata_path: str
    word_count: int
    local_links: int
    external_links: int
    table_count: int
    quality: str
    discard_reason: str | None


NOISE_PATTERNS = [
    '查看 "" 全部搜索结果',
    "AI 助理",
    "复制 MD 格式",
    "更新时间：",
    "[我的收藏]",
    "[产品详情]",
    "[首页]",
]

INTERFACE_REFERENCE_TITLE_PATTERNS = [
    "API参考",
    "API 概览",
    "OpenAPI",
    "SDK参考",
    "SDK 参考",
    "接口调用",
]

INTERFACE_REFERENCE_URL_SEGMENTS = {
    "assistantapi",
    "developer-reference",
    "list-of-operations-by-function",
    "sdk-reference",
}


def main() -> None:
    args = _parse_args()
    repo_root = Path(__file__).resolve().parents[4]
    data_root = repo_root / "data" / "datasources" / "aliyun-docs"
    manifest_path = data_root / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    documents = _read_documents(manifest)

    cleaned_documents: list[CleanedDocument] = []
    candidate_documents: list[CleanedDocument] = []
    discarded_documents: list[CleanedDocument] = []
    for cleaned_document in _clean_documents_concurrently(
        data_root=data_root,
        documents=documents,
        workers=args.workers,
    ):
        if cleaned_document.quality == "accepted":
            cleaned_documents.append(cleaned_document)
        elif cleaned_document.quality == "candidate":
            candidate_documents.append(cleaned_document)
        else:
            discarded_documents.append(cleaned_document)

    _write_cleaned_manifest(data_root=data_root, documents=cleaned_documents)
    _write_candidate_manifest(data_root=data_root, documents=candidate_documents)
    _write_quality_report(
        data_root=data_root,
        accepted_documents=cleaned_documents,
        candidate_documents=candidate_documents,
        discarded_documents=discarded_documents,
    )
    print(f"accepted: {len(cleaned_documents)}")
    print(f"candidate: {len(candidate_documents)}")
    print(f"discarded: {len(discarded_documents)}")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean crawled Aliyun documentation concurrently.")
    parser.add_argument("--workers", type=int, default=_default_workers(), help="Number of concurrent file workers.")
    return parser.parse_args()


def _default_workers() -> int:
    cpu_count = os.cpu_count() or 4
    return max(1, min(cpu_count, 8))


def _clean_documents_concurrently(
    data_root: Path,
    documents: list[dict[str, str]],
    workers: int,
) -> list[CleanedDocument]:
    if workers <= 0:
        raise ValueError("workers must be greater than 0")
    if workers == 1:
        return [clean_document(data_root=data_root, document=document) for document in documents]

    results_by_index: dict[int, CleanedDocument] = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(clean_document, data_root=data_root, document=document): index
            for index, document in enumerate(documents)
        }
        for future in as_completed(futures):
            results_by_index[futures[future]] = future.result()
    return [results_by_index[index] for index in range(len(documents))]


def clean_document(data_root: Path, document: dict[str, str]) -> CleanedDocument:
    source_path = Path(document["document_path"])
    if _is_interface_reference_document(document=document, source_path=source_path):
        output_path = _output_document_path(data_root=data_root, source_path=source_path, quality="discarded")
        metadata_path = _output_metadata_path(data_root=data_root, document_path=output_path, quality="discarded")
        return CleanedDocument(
            id=document["id"],
            product=document["product"],
            topic=document.get("topic", "features"),
            title=document["title"],
            source_url=document["url"],
            raw_document_path=document["document_path"],
            cleaned_document_path=str(output_path),
            metadata_path=str(metadata_path),
            word_count=0,
            local_links=0,
            external_links=0,
            table_count=0,
            quality="discarded",
            discard_reason="interface_reference",
        )
    if _is_anti_bot_document(document):
        output_path = _output_document_path(data_root=data_root, source_path=source_path, quality="discarded")
        metadata_path = _output_metadata_path(data_root=data_root, document_path=output_path, quality="discarded")
        return CleanedDocument(
            id=document["id"],
            product=document["product"],
            topic=document.get("topic", "features"),
            title=document["title"],
            source_url=document["url"],
            raw_document_path=document["document_path"],
            cleaned_document_path=str(output_path),
            metadata_path=str(metadata_path),
            word_count=0,
            local_links=0,
            external_links=0,
            table_count=0,
            quality="discarded",
            discard_reason="anti_bot_page",
        )

    markdown = source_path.read_text(encoding="utf-8")
    cleaned_markdown = clean_markdown(markdown=markdown, source_path=source_path, data_root=data_root)

    word_count = _word_count(cleaned_markdown)
    text_units = _content_text_units(cleaned_markdown)
    table_count = cleaned_markdown.count("| ---")
    local_links = cleaned_markdown.count("](../") + cleaned_markdown.count("](./")
    total_links = cleaned_markdown.count("](")
    external_links = max(total_links - local_links, 0)
    quality, discard_reason = _quality(
        cleaned_markdown=cleaned_markdown,
        text_units=text_units,
        table_count=table_count,
    )

    output_path = _output_document_path(data_root=data_root, source_path=source_path, quality=quality)
    metadata_path = _output_metadata_path(data_root=data_root, document_path=output_path, quality=quality)
    if quality in {"accepted", "candidate"}:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(cleaned_markdown, encoding="utf-8")

        metadata = {
            "id": document["id"],
            "source": document.get("source", "aliyun_docs"),
            "product": document["product"],
            "topic": document.get("topic", "features"),
            "title": document["title"],
            "source_url": document["url"],
            "raw_document_path": document["document_path"],
            "output_document_path": str(output_path),
            "word_count": word_count,
            "text_units": text_units,
            "local_links": local_links,
            "external_links": external_links,
            "has_tables": table_count > 0,
            "table_count": table_count,
            "quality": quality,
        }
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    return CleanedDocument(
        id=document["id"],
        product=document["product"],
        topic=document.get("topic", "features"),
        title=document["title"],
        source_url=document["url"],
        raw_document_path=document["document_path"],
        cleaned_document_path=str(output_path),
        metadata_path=str(metadata_path),
        word_count=word_count,
        local_links=local_links,
        external_links=external_links,
        table_count=table_count,
        quality=quality,
        discard_reason=discard_reason,
    )


def clean_markdown(markdown: str, source_path: Path, data_root: Path) -> str:
    lines = markdown.splitlines()
    title = lines[0].strip() if lines and lines[0].startswith("# ") else "# Untitled"
    source = next((line.strip() for line in lines if line.startswith("Source: ")), "")
    body_lines = _article_body_lines(lines)

    cleaned_lines: list[str] = [title, "", source, ""]
    for line in body_lines:
        cleaned_line = _clean_line(line.strip())
        if not cleaned_line:
            continue
        cleaned_line = _rewrite_local_links(cleaned_line, source_path=source_path, data_root=data_root)
        cleaned_lines.append(cleaned_line)

    return _compact_blank_lines(cleaned_lines)


def _article_body_lines(lines: list[str]) -> list[str]:
    source_index = next((index for index, line in enumerate(lines) if line.startswith("Source: ")), 0)
    content_lines = lines[source_index + 1 :]
    for index, line in enumerate(content_lines):
        stripped = line.strip()
        if stripped.startswith("# ") and "https://help.aliyun.com" not in stripped:
            return content_lines[index:]
    return content_lines


def _clean_line(line: str) -> str | None:
    if not line:
        return ""
    if line in {"-", "- "}:
        return None
    if "上一篇" in line or "下一篇" in line:
        return None
    if any(pattern in line for pattern in NOISE_PATTERNS):
        return None
    if line.startswith("[大模型]") or line.startswith("[文档]"):
        return None
    return line


def _rewrite_local_links(line: str, source_path: Path, data_root: Path) -> str:
    link_pattern = re.compile(r"\]\((products/[^)]+\.md)\)")

    def replace_link(match: re.Match[str]) -> str:
        target = data_root / match.group(1)
        target_cleaned = _cleaned_document_path(data_root=data_root, source_path=target)
        source_cleaned = _cleaned_document_path(data_root=data_root, source_path=source_path)
        relative_target = _relative_link(from_path=source_cleaned, to_path=target_cleaned)
        return f"]({relative_target})"

    return link_pattern.sub(replace_link, line)


def _relative_link(from_path: Path, to_path: Path) -> str:
    return Path(os.path.relpath(to_path, start=from_path.parent)).as_posix()


def _cleaned_document_path(data_root: Path, source_path: Path) -> Path:
    relative_path = source_path.relative_to(data_root / "products")
    return data_root / "cleaned" / "products" / relative_path


def _candidate_document_path(data_root: Path, source_path: Path) -> Path:
    relative_path = source_path.relative_to(data_root / "products")
    return data_root / "candidates" / "products" / relative_path


def _output_document_path(data_root: Path, source_path: Path, quality: str) -> Path:
    if quality == "candidate":
        return _candidate_document_path(data_root=data_root, source_path=source_path)
    return _cleaned_document_path(data_root=data_root, source_path=source_path)


def _output_metadata_path(data_root: Path, document_path: Path, quality: str) -> Path:
    layer = "candidates" if quality == "candidate" else "cleaned"
    relative_path = document_path.relative_to(data_root / layer / "products")
    parts = list(relative_path.parts)
    if len(parts) >= 2 and parts[1] == "documents":
        parts[1] = "metadata"
    return data_root / layer / "products" / Path(*parts).with_suffix(".json")


def _compact_blank_lines(lines: list[str]) -> str:
    compacted_lines: list[str] = []
    previous_blank = False
    for line in lines:
        is_blank = line == ""
        if is_blank and previous_blank:
            continue
        compacted_lines.append(line)
        previous_blank = is_blank
    return "\n".join(compacted_lines).strip() + "\n"


def _word_count(markdown: str) -> int:
    return len(re.findall(r"[\w\u4e00-\u9fff]+", markdown))


def _text_units(markdown: str) -> int:
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", markdown))
    latin_words = len(re.findall(r"[A-Za-z0-9_]+", markdown))
    return chinese_chars + latin_words


def _content_text_units(markdown: str) -> int:
    content_lines = [
        line
        for line in markdown.splitlines()
        if line.strip() and not line.startswith("# ") and not line.startswith("Source: ")
    ]
    return _text_units("\n".join(content_lines))


def _quality(cleaned_markdown: str, text_units: int, table_count: int) -> tuple[str, str | None]:
    if text_units < 40 and table_count == 0:
        return "discarded", "too_short"
    local_links = cleaned_markdown.count("](")
    if text_units < 120 and table_count == 0:
        return "candidate", "short_but_reviewable"
    if text_units < 240 and local_links > 8 and table_count == 0:
        return "candidate", "directory_like"
    if text_units < 240 and table_count == 0:
        return "candidate", "medium_confidence"
    return "accepted", None


def _is_interface_reference_document(document: dict[str, str], source_path: Path) -> bool:
    title = document.get("title", "")
    if any(pattern in title for pattern in INTERFACE_REFERENCE_TITLE_PATTERNS):
        return True

    source_url = document.get("url", "")
    url_segments = [segment.lower() for segment in source_url.split("/") if segment]
    path_segments = [part.lower() for part in source_path.parts]
    segments = url_segments + path_segments
    for segment in segments:
        if segment in INTERFACE_REFERENCE_URL_SEGMENTS:
            return True
        if segment.startswith("api-") or segment.endswith("-api"):
            return True
        if "api-reference" in segment or "openapi" in segment:
            return True
    return False


def _is_anti_bot_document(document: dict[str, str]) -> bool:
    raw_path_value = document.get("raw_path")
    if not raw_path_value:
        return False
    raw_path = Path(raw_path_value)
    if not raw_path.exists():
        return False
    return is_aliyun_anti_bot_page(raw_path.read_text(encoding="utf-8", errors="ignore"))


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


def _write_cleaned_manifest(data_root: Path, documents: list[CleanedDocument]) -> None:
    manifest = {
        "source": "aliyun_docs",
        "documents": [
            {
                "id": document.id,
                "product": document.product,
                "topic": document.topic,
                "title": document.title,
                "source_url": document.source_url,
                "cleaned_document_path": document.cleaned_document_path,
                "metadata_path": document.metadata_path,
                "word_count": document.word_count,
                "table_count": document.table_count,
            }
            for document in documents
        ],
    }
    (data_root / "cleaned-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _write_candidate_manifest(data_root: Path, documents: list[CleanedDocument]) -> None:
    manifest = {
        "source": "aliyun_docs",
        "documents": [
            {
                "id": document.id,
                "product": document.product,
                "topic": document.topic,
                "title": document.title,
                "source_url": document.source_url,
                "candidate_document_path": document.cleaned_document_path,
                "metadata_path": document.metadata_path,
                "word_count": document.word_count,
                "table_count": document.table_count,
                "candidate_reason": document.discard_reason,
            }
            for document in documents
        ],
    }
    (data_root / "candidate-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _write_quality_report(
    data_root: Path,
    accepted_documents: list[CleanedDocument],
    candidate_documents: list[CleanedDocument],
    discarded_documents: list[CleanedDocument],
) -> None:
    report = {
        "source": "aliyun_docs",
        "accepted": len(accepted_documents),
        "candidate": len(candidate_documents),
        "discarded": len(discarded_documents),
        "accepted_by_product": dict(sorted(Counter(document.product for document in accepted_documents).items())),
        "candidate_by_product": dict(sorted(Counter(document.product for document in candidate_documents).items())),
        "candidate_by_reason": dict(
            sorted(Counter(document.discard_reason for document in candidate_documents).items())
        ),
        "discarded_by_reason": dict(
            sorted(Counter(document.discard_reason for document in discarded_documents).items())
        ),
        "accepted_by_topic": dict(sorted(Counter(document.topic for document in accepted_documents).items())),
        "candidate_by_topic": dict(sorted(Counter(document.topic for document in candidate_documents).items())),
        "documents_with_tables": sum(1 for document in accepted_documents if document.table_count > 0),
        "candidate_documents_with_tables": sum(1 for document in candidate_documents if document.table_count > 0),
        "total_tables": sum(document.table_count for document in accepted_documents),
        "candidate_total_tables": sum(document.table_count for document in candidate_documents),
        "total_local_links": sum(document.local_links for document in accepted_documents),
        "candidate_total_local_links": sum(document.local_links for document in candidate_documents),
        "total_external_links": sum(document.external_links for document in accepted_documents),
        "candidate_total_external_links": sum(document.external_links for document in candidate_documents),
    }
    (data_root / "quality-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
