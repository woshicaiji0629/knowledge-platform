from knowledge_platform.crawlers.aliyun_docs import AliyunDocsCrawler
from knowledge_platform.llm.intent import RuleBasedIntentClassifier
from knowledge_platform.services.chat_service import ChatService
from knowledge_platform.services.ingestion_service import IngestionService
from knowledge_platform.services.retrieval_service import RetrievalService
from knowledge_platform.sessions.store import session_store
from knowledge_platform.vectorstores.memory import MemoryVectorStore


vector_store = MemoryVectorStore()


def create_chat_service() -> ChatService:
    return ChatService(
        session_store=session_store,
        retrieval_service=RetrievalService(vector_store=vector_store),
        intent_classifier=RuleBasedIntentClassifier(),
    )


def create_ingestion_service() -> IngestionService:
    return IngestionService(aliyun_docs_crawler=AliyunDocsCrawler())
