from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from knowledge_platform.services.factory import create_ingestion_service

router = APIRouter()


class AliyunDocsIngestionPlanRequest(BaseModel):
    seed_urls: list[str] = Field(min_length=1)
    max_pages: int = Field(default=20, ge=1, le=500)
    max_depth: int = Field(default=1, ge=0, le=5)


class CrawlPlanResponse(BaseModel):
    source: str
    seed_urls: list[str]
    allowed_domains: list[str]
    max_pages: int
    max_depth: int


class IngestionPlanResponse(BaseModel):
    plan: CrawlPlanResponse
    status: str
    message: str


class CrawledDocumentResponse(BaseModel):
    id: str
    source: str
    url: str
    title: str
    raw_path: str | None = None
    metadata_path: str | None = None


class IngestionCrawlResponse(BaseModel):
    documents: list[CrawledDocumentResponse]
    status: str
    message: str


@router.post("/aliyun-docs/plan", response_model=IngestionPlanResponse)
def plan_aliyun_docs_ingestion(request: AliyunDocsIngestionPlanRequest) -> IngestionPlanResponse:
    try:
        result = create_ingestion_service().plan_aliyun_docs_ingestion(
            seed_urls=request.seed_urls,
            max_pages=request.max_pages,
            max_depth=request.max_depth,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    return IngestionPlanResponse(
        plan=CrawlPlanResponse(
            source=result.plan.source,
            seed_urls=result.plan.seed_urls,
            allowed_domains=result.plan.allowed_domains,
            max_pages=result.plan.max_pages,
            max_depth=result.plan.max_depth,
        ),
        status=result.status,
        message=result.message,
    )


@router.post("/aliyun-docs/crawl", response_model=IngestionCrawlResponse)
def crawl_aliyun_docs(request: AliyunDocsIngestionPlanRequest) -> IngestionCrawlResponse:
    try:
        result = create_ingestion_service().crawl_aliyun_docs(
            seed_urls=request.seed_urls,
            max_pages=request.max_pages,
            max_depth=request.max_depth,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc

    return IngestionCrawlResponse(
        documents=[
            CrawledDocumentResponse(
                id=document.id,
                source=document.source,
                url=document.url,
                title=document.title,
                raw_path=document.metadata.get("raw_path"),
                metadata_path=document.metadata.get("metadata_path"),
            )
            for document in result.documents
        ],
        status=result.status,
        message=result.message,
    )
