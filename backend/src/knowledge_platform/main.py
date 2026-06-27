from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from knowledge_platform.api.v1.router import router as v1_router
from knowledge_platform.config.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "environment": settings.app_env}

    app.include_router(v1_router, prefix="/api/v1")
    return app


app = create_app()
