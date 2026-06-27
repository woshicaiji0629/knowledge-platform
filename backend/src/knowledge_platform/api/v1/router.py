from fastapi import APIRouter

from knowledge_platform.api.v1.routes import chat, customer_service, ingestion

router = APIRouter()
router.include_router(chat.router, prefix="/chat", tags=["chat"])
router.include_router(customer_service.router, prefix="/customer-service", tags=["customer-service"])
router.include_router(ingestion.router, prefix="/ingestion", tags=["ingestion"])
