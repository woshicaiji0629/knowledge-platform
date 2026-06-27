from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "knowledge-platform"
    app_env: str = "local"
    log_level: str = "INFO"
    cors_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    aliyun_customer_service_endpoint: str | None = None
    aliyun_access_key_id: str | None = None
    aliyun_access_key_secret: str | None = None
    aliyun_customer_service_instance_id: str | None = None

    vector_store_provider: str = "memory"
    qdrant_endpoint: str = "http://localhost:6333"
    qdrant_collection: str = "aliyun_docs_product_v1"
    retrieval_top_k: int = 5
    retrieval_context_max_chars: int = 6000
    answer_generator_provider: str = "skeleton"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()
