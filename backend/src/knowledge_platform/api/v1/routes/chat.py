from datetime import datetime

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from knowledge_platform.services.factory import create_chat_service
from knowledge_platform.sessions.models import ChatMessage, ChatSession, Citation
from knowledge_platform.sessions.store import session_store

router = APIRouter()


class CitationResponse(BaseModel):
    title: str
    url: str
    source: str
    score: float


class ChatMessageResponse(BaseModel):
    id: str
    role: str
    content: str
    created_at: datetime
    citations: list[CitationResponse]
    intent: str | None = None


class ChatSessionResponse(BaseModel):
    id: str
    title: str
    created_at: datetime
    updated_at: datetime
    messages: list[ChatMessageResponse]


class SendMessageRequest(BaseModel):
    message: str = Field(min_length=1)


class SendMessageResponse(BaseModel):
    session: ChatSessionResponse
    message: ChatMessageResponse


@router.get("/sessions", response_model=list[ChatSessionResponse])
def list_sessions() -> list[ChatSessionResponse]:
    return [_to_session_response(session) for session in session_store.list_sessions()]


@router.get("/sessions/{session_id}", response_model=ChatSessionResponse)
def get_session(session_id: str) -> ChatSessionResponse:
    session = session_store.get(session_id)
    if session is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat session not found")
    return _to_session_response(session)


@router.post("/sessions/{session_id}/messages", response_model=SendMessageResponse)
async def send_message(session_id: str, request: SendMessageRequest) -> SendMessageResponse:
    result = await create_chat_service().send_message(session_id=session_id, message=request.message)
    return SendMessageResponse(
        session=_to_session_response(result.session),
        message=_to_message_response(result.assistant_message),
    )


def _to_session_response(session: ChatSession) -> ChatSessionResponse:
    return ChatSessionResponse(
        id=session.id,
        title=session.title,
        created_at=session.created_at,
        updated_at=session.updated_at,
        messages=[_to_message_response(message) for message in session.messages],
    )


def _to_message_response(message: ChatMessage) -> ChatMessageResponse:
    return ChatMessageResponse(
        id=message.id,
        role=message.role.value,
        content=message.content,
        created_at=message.created_at,
        citations=[_to_citation_response(citation) for citation in message.citations],
        intent=message.intent,
    )


def _to_citation_response(citation: Citation) -> CitationResponse:
    return CitationResponse(
        title=citation.title,
        url=citation.url,
        source=citation.source,
        score=citation.score,
    )
