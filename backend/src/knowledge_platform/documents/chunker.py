from knowledge_platform.documents.models import DocumentChunk, RawDocument


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
