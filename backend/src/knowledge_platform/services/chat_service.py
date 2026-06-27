from dataclasses import dataclass
from uuid import uuid4

from knowledge_platform.llm.answer import AnswerGenerationRequest, AnswerGeneratorProtocol
from knowledge_platform.llm.intent import RuleBasedIntentClassifier
from knowledge_platform.services.retrieval_service import (
    RetrievalQuality,
    RetrievalServiceProtocol,
    evaluate_retrieval_quality,
)
from knowledge_platform.sessions.models import ChatMessage, ChatSession, MessageRole
from knowledge_platform.sessions.store import InMemorySessionStore


@dataclass(frozen=True)
class ChatTurnResult:
    session: ChatSession
    assistant_message: ChatMessage
    quality: RetrievalQuality


class ChatService:
    def __init__(
        self,
        session_store: InMemorySessionStore,
        retrieval_service: RetrievalServiceProtocol,
        answer_generator: AnswerGeneratorProtocol,
        intent_classifier: RuleBasedIntentClassifier,
    ) -> None:
        self._session_store = session_store
        self._retrieval_service = retrieval_service
        self._answer_generator = answer_generator
        self._intent_classifier = intent_classifier

    async def send_message(
        self,
        session_id: str,
        message: str,
        product_filter: str | None = None,
    ) -> ChatTurnResult:
        intent = self._intent_classifier.classify(message)
        user_message = ChatMessage(
            id=str(uuid4()),
            role=MessageRole.USER,
            content=message,
            intent=intent.intent.value,
        )
        self._session_store.append_message(session_id=session_id, message=user_message)

        retrieval_context = await self._retrieval_service.retrieve(query=message, product_filter=product_filter)
        quality = evaluate_retrieval_quality(
            citations=retrieval_context.citations,
            product_filter=product_filter,
        )
        answer = await self._answer_generator.generate(
            AnswerGenerationRequest(
                question=message,
                context_text=retrieval_context.context_text,
                citations=retrieval_context.citations,
            )
        )
        assistant_message = ChatMessage(
            id=str(uuid4()),
            role=MessageRole.ASSISTANT,
            content=answer,
            citations=retrieval_context.citations,
            intent=intent.intent.value,
        )
        session = self._session_store.append_message(session_id=session_id, message=assistant_message)
        return ChatTurnResult(session=session, assistant_message=assistant_message, quality=quality)
