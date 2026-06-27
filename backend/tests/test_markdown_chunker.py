from datetime import UTC, datetime

import pytest

from knowledge_platform.documents.chunker import MarkdownChunker, create_chunker
from knowledge_platform.documents.models import RawDocument


def test_markdown_chunker_keeps_heading_path() -> None:
    document = RawDocument(
        id="aliyun:ecs:test",
        source="aliyun_docs",
        url="https://help.aliyun.com/zh/ecs/test",
        title="ECS Test",
        content="# ECS Test\n\nSource: https://help.aliyun.com/zh/ecs/test\n\n## 创建实例\n\n正文内容。",
        fetched_at=datetime.now(UTC),
        metadata={"product": "ecs", "topic": "deployment"},
    )

    chunks = MarkdownChunker(max_chars=80, overlap_chars=10, min_content_chars=1).split(document)

    assert chunks
    assert chunks[-1].metadata["heading_path"] == "ECS Test > 创建实例"
    assert chunks[-1].metadata["product"] == "ecs"


def test_markdown_chunker_keeps_table_block_together() -> None:
    document = RawDocument(
        id="aliyun:ecs:table",
        source="aliyun_docs",
        url="https://help.aliyun.com/zh/ecs/table",
        title="ECS Table",
        content=(
            "# ECS Table\n\n"
            "## 规格\n\n"
            "规格说明。\n\n"
            "| 名称 | 说明 |\n"
            "| --- | --- |\n"
            "| ecs.g8i | 通用型实例 |\n\n"
            "后续说明。"
        ),
        fetched_at=datetime.now(UTC),
        metadata={"product": "ecs", "topic": "performance"},
    )

    chunks = MarkdownChunker(max_chars=60, overlap_chars=8).split(document)

    table_chunks = [chunk for chunk in chunks if "| 名称 | 说明 |" in chunk.content]
    assert len(table_chunks) == 1
    assert "| ecs.g8i | 通用型实例 |" in table_chunks[0].content


def test_create_chunker_uses_registered_strategy() -> None:
    chunker = create_chunker(
        name="markdown-heading-table-preserve",
        max_chars=80,
        overlap_chars=10,
        min_content_chars=1,
    )
    document = RawDocument(
        id="aliyun:ecs:registered",
        source="aliyun_docs",
        url="https://help.aliyun.com/zh/ecs/registered",
        title="ECS Registered",
        content="# ECS Registered\n\n## 概述\n\n正文内容。",
        fetched_at=datetime.now(UTC),
        metadata={},
    )

    assert chunker.split(document)


def test_create_chunker_rejects_unknown_strategy() -> None:
    with pytest.raises(ValueError, match="unknown chunker"):
        create_chunker(name="unknown", max_chars=80, overlap_chars=10)
