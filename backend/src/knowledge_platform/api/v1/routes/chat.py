from datetime import datetime

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from knowledge_platform.services.factory import create_chat_service
from knowledge_platform.services.retrieval_service import RetrievalQuality
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
    product_filter: str | None = None


class RetrievalQualityResponse(BaseModel):
    target_product_citations: int
    off_product_citations: int
    interface_reference_citations: int
    top_score: float
    avg_score: float
    quality_warnings: list[str]


class SendMessageResponse(BaseModel):
    session: ChatSessionResponse
    message: ChatMessageResponse
    quality: RetrievalQualityResponse


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
    result = await create_chat_service().send_message(
        session_id=session_id,
        message=request.message,
        product_filter=request.product_filter,
    )
    return SendMessageResponse(
        session=_to_session_response(result.session),
        message=_to_message_response(result.assistant_message),
        quality=_to_quality_response(result.quality),
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


def _to_quality_response(quality: RetrievalQuality) -> RetrievalQualityResponse:
    return RetrievalQualityResponse(
        target_product_citations=quality.target_product_citations,
        off_product_citations=quality.off_product_citations,
        interface_reference_citations=quality.interface_reference_citations,
        top_score=quality.top_score,
        avg_score=quality.avg_score,
        quality_warnings=quality.quality_warnings,
    )
