from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum


def _empty_citations() -> list["Citation"]:
    return []


def _empty_messages() -> list["ChatMessage"]:
    return []


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
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    citations: list[Citation] = field(default_factory=_empty_citations)
    intent: str | None = None


@dataclass
class ChatSession:
    id: str
    title: str
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    messages: list[ChatMessage] = field(default_factory=_empty_messages)
