from knowledge_platform.config.settings import get_settings
from knowledge_platform.crawlers.aliyun_docs import AliyunDocsCrawler
from knowledge_platform.embeddings.dashscope import DashScopeEmbeddingProvider, dashscope_config_from_env
from knowledge_platform.llm.intent import RuleBasedIntentClassifier
from knowledge_platform.services.chat_service import ChatService
from knowledge_platform.services.ingestion_service import IngestionService
from knowledge_platform.services.retrieval_service import (
    QdrantRetrievalService,
    RetrievalService,
    RetrievalServiceProtocol,
)
from knowledge_platform.sessions.store import session_store
from knowledge_platform.vectorstores.memory import MemoryVectorStore
from knowledge_platform.vectorstores.qdrant import QdrantConfig, QdrantVectorStore

vector_store = MemoryVectorStore()


def create_chat_service() -> ChatService:
    return ChatService(
        session_store=session_store,
        retrieval_service=_create_retrieval_service(),
        intent_classifier=RuleBasedIntentClassifier(),
    )


def create_ingestion_service() -> IngestionService:
    return IngestionService(aliyun_docs_crawler=AliyunDocsCrawler())


def _create_retrieval_service() -> RetrievalServiceProtocol:
    settings = get_settings()
    provider = settings.vector_store_provider.lower()

    if provider == "qdrant":
        return QdrantRetrievalService(
            embedding_provider=DashScopeEmbeddingProvider(config=dashscope_config_from_env()),
            vector_store=QdrantVectorStore(
                config=QdrantConfig(
                    endpoint=settings.qdrant_endpoint,
                    collection_name=settings.qdrant_collection,
                )
            ),
            default_limit=settings.retrieval_top_k,
            context_max_chars=settings.retrieval_context_max_chars,
        )

    if provider != "memory":
        raise ValueError(f"Unsupported vector store provider: {settings.vector_store_provider}")

    return RetrievalService(
        vector_store=vector_store,
        default_limit=settings.retrieval_top_k,
        context_max_chars=settings.retrieval_context_max_chars,
    )
