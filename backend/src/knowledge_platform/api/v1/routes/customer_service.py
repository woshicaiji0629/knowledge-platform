from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from knowledge_platform.config.settings import get_settings
from knowledge_platform.providers.aliyun_customer_service import AliyunCustomerServiceProvider
from knowledge_platform.providers.base import ProviderNotConfiguredError
from knowledge_platform.services.customer_service import CustomerService

router = APIRouter()


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)
    session_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
    provider: str
    session_id: str | None = None


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    settings = get_settings()
    provider = AliyunCustomerServiceProvider(settings=settings)
    service = CustomerService(provider=provider)

    try:
        result = service.chat(message=request.message, session_id=request.session_id)
    except ProviderNotConfiguredError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc

    return ChatResponse(
        answer=result.answer,
        provider=result.provider,
        session_id=result.session_id,
    )
