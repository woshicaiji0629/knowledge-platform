from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class RawDocument:
    id: str
    source: str
    url: str
    title: str
    content: str
    fetched_at: datetime
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class DocumentChunk:
    id: str
    document_id: str
    source: str
    url: str
    title: str
    content: str
    chunk_index: int
    metadata: dict[str, str] = field(default_factory=dict)
