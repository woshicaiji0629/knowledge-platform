from collections.abc import Callable
from typing import Protocol

from knowledge_platform.documents.models import DocumentChunk, RawDocument


class DocumentChunker(Protocol):
    def split(self, document: RawDocument) -> list[DocumentChunk]:
        raise NotImplementedError


class CharacterChunker:
    def __init__(self, max_chars: int = 1200, overlap_chars: int = 160) -> None:
        if max_chars <= 0:
            raise ValueError("max_chars must be greater than 0")
        if overlap_chars < 0:
            raise ValueError("overlap_chars must be greater than or equal to 0")
        if overlap_chars >= max_chars:
            raise ValueError("overlap_chars must be smaller than max_chars")

        self._max_chars = max_chars
        self._overlap_chars = overlap_chars

    def split(self, document: RawDocument) -> list[DocumentChunk]:
        normalized_content = " ".join(document.content.split())
        if not normalized_content:
            return []

        chunks: list[DocumentChunk] = []
        start = 0
        while start < len(normalized_content):
            end = min(start + self._max_chars, len(normalized_content))
            content = normalized_content[start:end]
            chunks.append(
                DocumentChunk(
                    id=f"{document.id}:{len(chunks)}",
                    document_id=document.id,
                    source=document.source,
                    url=document.url,
                    title=document.title,
                    content=content,
                    chunk_index=len(chunks),
                    metadata=document.metadata,
                )
            )
            if end == len(normalized_content):
                break
            start = end - self._overlap_chars

        return chunks


class MarkdownChunker:
    def __init__(self, max_chars: int = 1200, overlap_chars: int = 160, min_content_chars: int = 80) -> None:
        if max_chars <= 0:
            raise ValueError("max_chars must be greater than 0")
        if overlap_chars < 0:
            raise ValueError("overlap_chars must be greater than or equal to 0")
        if overlap_chars >= max_chars:
            raise ValueError("overlap_chars must be smaller than max_chars")
        if min_content_chars < 0:
            raise ValueError("min_content_chars must be greater than or equal to 0")

        self._max_chars = max_chars
        self._overlap_chars = overlap_chars
        self._min_content_chars = min_content_chars

    def split(self, document: RawDocument) -> list[DocumentChunk]:
        sections = _markdown_sections(document.content)
        chunks: list[DocumentChunk] = []
        for heading_path, section_text in sections:
            for content in self._split_section(section_text):
                if not _is_informative_chunk(content, self._min_content_chars):
                    continue
                metadata = dict(document.metadata)
                metadata["heading_path"] = " > ".join(heading_path)
                chunks.append(
                    DocumentChunk(
                        id=f"{document.id}:{len(chunks)}",
                        document_id=document.id,
                        source=document.source,
                        url=document.url,
                        title=document.title,
                        content=content,
                        chunk_index=len(chunks),
                        metadata=metadata,
                    )
                )
        return chunks

    def _split_section(self, section_text: str) -> list[str]:
        blocks = _markdown_blocks(section_text)
        chunks: list[str] = []
        current_blocks: list[str] = []
        current_size = 0
        for block in blocks:
            block_size = len(block)
            if block_size > self._max_chars:
                if current_blocks:
                    chunks.append("\n\n".join(current_blocks).strip())
                    current_blocks = []
                    current_size = 0
                chunks.extend(_split_long_text(block, max_chars=self._max_chars, overlap_chars=self._overlap_chars))
                continue

            next_size = current_size + block_size + (2 if current_blocks else 0)
            if current_blocks and next_size > self._max_chars:
                chunks.append("\n\n".join(current_blocks).strip())
                overlap = _overlap_suffix(current_blocks, self._overlap_chars)
                current_blocks = [overlap] if overlap else []
                current_size = len(overlap) if overlap else 0

            current_blocks.append(block)
            current_size += block_size + (2 if current_blocks else 0)

        if current_blocks:
            chunks.append("\n\n".join(current_blocks).strip())
        return [chunk for chunk in chunks if chunk]


def _markdown_sections(markdown: str) -> list[tuple[list[str], str]]:
    sections: list[tuple[list[str], list[str]]] = []
    heading_stack: list[str] = []
    current_lines: list[str] = []
    current_heading_path: list[str] = []

    for line in markdown.splitlines():
        heading_level = _heading_level(line)
        if heading_level is not None:
            if current_lines:
                sections.append((current_heading_path, current_lines))
                current_lines = []
            heading_text = line.lstrip("#").strip()
            heading_stack = heading_stack[: heading_level - 1]
            heading_stack.append(heading_text)
            current_heading_path = list(heading_stack)
        current_lines.append(line)

    if current_lines:
        sections.append((current_heading_path, current_lines))

    return [(heading_path, "\n".join(lines).strip()) for heading_path, lines in sections if "\n".join(lines).strip()]


def _heading_level(line: str) -> int | None:
    stripped = line.lstrip()
    if not stripped.startswith("#"):
        return None
    marker = stripped.split(" ", maxsplit=1)[0]
    if not marker or any(char != "#" for char in marker):
        return None
    level = len(marker)
    if level > 6:
        return None
    return level


def _markdown_blocks(markdown: str) -> list[str]:
    blocks: list[str] = []
    current_lines: list[str] = []
    table_lines: list[str] = []

    for line in markdown.splitlines():
        if _is_table_line(line):
            if current_lines:
                blocks.append("\n".join(current_lines).strip())
                current_lines = []
            table_lines.append(line)
            continue

        if table_lines:
            blocks.append("\n".join(table_lines).strip())
            table_lines = []

        if not line.strip():
            if current_lines:
                blocks.append("\n".join(current_lines).strip())
                current_lines = []
            continue

        current_lines.append(line)

    if table_lines:
        blocks.append("\n".join(table_lines).strip())
    if current_lines:
        blocks.append("\n".join(current_lines).strip())

    return [block for block in blocks if block]


def _is_table_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|")


def _split_long_text(text: str, max_chars: int, overlap_chars: int) -> list[str]:
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        chunks.append(text[start:end].strip())
        if end == len(text):
            break
        start = end - overlap_chars
    return [chunk for chunk in chunks if chunk]


def _overlap_suffix(blocks: list[str], overlap_chars: int) -> str:
    if overlap_chars == 0:
        return ""
    text = "\n\n".join(blocks)
    return text[-overlap_chars:].strip()


def _is_informative_chunk(markdown: str, min_content_chars: int) -> bool:
    if _contains_table(markdown):
        return True
    content_lines = [
        line.strip()
        for line in markdown.splitlines()
        if line.strip() and not line.startswith("#") and not line.startswith("Source: ")
    ]
    return len("".join(content_lines)) >= min_content_chars


def _contains_table(markdown: str) -> bool:
    return any(_is_table_line(line) for line in markdown.splitlines())


ChunkerFactory = Callable[[int, int, int], DocumentChunker]


def create_chunker(name: str, max_chars: int, overlap_chars: int, min_content_chars: int = 80) -> DocumentChunker:
    normalized_name = name.strip().lower().replace("_", "-")
    factories: dict[str, ChunkerFactory] = {
        "character": lambda max_chars, overlap_chars, _min_content_chars: CharacterChunker(
            max_chars=max_chars,
            overlap_chars=overlap_chars,
        ),
        "markdown": lambda max_chars, overlap_chars, min_content_chars: MarkdownChunker(
            max_chars=max_chars,
            overlap_chars=overlap_chars,
            min_content_chars=min_content_chars,
        ),
        "markdown-heading": lambda max_chars, overlap_chars, min_content_chars: MarkdownChunker(
            max_chars=max_chars,
            overlap_chars=overlap_chars,
            min_content_chars=min_content_chars,
        ),
        "markdown-heading-table-preserve": lambda max_chars, overlap_chars, min_content_chars: MarkdownChunker(
            max_chars=max_chars,
            overlap_chars=overlap_chars,
            min_content_chars=min_content_chars,
        ),
    }
    factory = factories.get(normalized_name)
    if factory is None:
        allowed = ", ".join(sorted(factories))
        raise ValueError(f"unknown chunker '{name}', expected one of: {allowed}")
    return factory(max_chars, overlap_chars, min_content_chars)
