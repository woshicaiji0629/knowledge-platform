from datetime import datetime, timezone

from knowledge_platform.sessions.models import ChatMessage, ChatSession, MessageRole


class InMemorySessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, ChatSession] = {}

    def list_sessions(self) -> list[ChatSession]:
        return sorted(self._sessions.values(), key=lambda session: session.updated_at, reverse=True)

    def get_or_create(self, session_id: str, title: str = "新会话") -> ChatSession:
        session = self._sessions.get(session_id)
        if session is not None:
            return session

        session = ChatSession(id=session_id, title=title)
        self._sessions[session_id] = session
        return session

    def get(self, session_id: str) -> ChatSession | None:
        return self._sessions.get(session_id)

    def append_message(self, session_id: str, message: ChatMessage) -> ChatSession:
        session = self.get_or_create(session_id=session_id)
        session.messages.append(message)
        session.updated_at = datetime.now(timezone.utc)
        if session.title == "新会话" and message.role == MessageRole.USER:
            session.title = message.content[:32]
        return session


session_store = InMemorySessionStore()
