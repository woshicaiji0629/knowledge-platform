from dataclasses import dataclass
from uuid import uuid4

from knowledge_platform.llm.intent import RuleBasedIntentClassifier
from knowledge_platform.services.retrieval_service import RetrievalService
from knowledge_platform.sessions.models import ChatMessage, ChatSession, MessageRole
from knowledge_platform.sessions.store import InMemorySessionStore


@dataclass(frozen=True)
class ChatTurnResult:
    session: ChatSession
    assistant_message: ChatMessage


class ChatService:
    def __init__(
        self,
        session_store: InMemorySessionStore,
        retrieval_service: RetrievalService,
        intent_classifier: RuleBasedIntentClassifier,
    ) -> None:
        self._session_store = session_store
        self._retrieval_service = retrieval_service
        self._intent_classifier = intent_classifier

    def send_message(self, session_id: str, message: str) -> ChatTurnResult:
        intent = self._intent_classifier.classify(message)
        user_message = ChatMessage(
            id=str(uuid4()),
            role=MessageRole.USER,
            content=message,
            intent=intent.intent.value,
        )
        self._session_store.append_message(session_id=session_id, message=user_message)

        retrieval_context = self._retrieval_service.retrieve(query=message)
        answer = self._build_skeleton_answer(message=message, context_text=retrieval_context.context_text)
        assistant_message = ChatMessage(
            id=str(uuid4()),
            role=MessageRole.ASSISTANT,
            content=answer,
            citations=retrieval_context.citations,
            intent=intent.intent.value,
        )
        session = self._session_store.append_message(session_id=session_id, message=assistant_message)
        return ChatTurnResult(session=session, assistant_message=assistant_message)

    def _build_skeleton_answer(self, message: str, context_text: str) -> str:
        if context_text:
            return f"已根据本地文档索引生成占位回答。问题：{message}"
        return "当前还没有可用的本地文档索引。请先运行阿里云官方文档采集和入库流程。"
