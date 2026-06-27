from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from knowledge_platform.api.v1.router import router as v1_router
from knowledge_platform.config.settings import get_settings


def health_response(environment: str) -> dict[str, str]:
    return {"status": "ok", "environment": environment}


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

    def health() -> dict[str, str]:
        return health_response(settings.app_env)

    app.add_api_route("/health", health, methods=["GET"])
    app.include_router(v1_router, prefix="/api/v1")
    return app


app = create_app()
