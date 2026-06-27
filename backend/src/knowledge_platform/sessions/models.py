from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum


class MessageRole(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


@dataclass(frozen=True)
class Citation:
    title: str
    url: str
    source: str
    score: float


@dataclass(frozen=True)
class ChatMessage:
    id: str
    role: MessageRole
    content: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    citations: list[Citation] = field(default_factory=list)
    intent: str | None = None


@dataclass
class ChatSession:
    id: str
    title: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    messages: list[ChatMessage] = field(default_factory=list)
