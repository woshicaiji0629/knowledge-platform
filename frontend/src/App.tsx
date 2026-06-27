import { FormEvent, useMemo, useState } from "react";

import { sendChatMessage } from "./api/chat";
import type { ChatMessage } from "./types";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [isSending, setIsSending] = useState(false);
  const sessionId = useMemo(() => crypto.randomUUID(), []);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const message = input.trim();
    if (!message || isSending) {
      return;
    }

    setError(null);
    setInput("");
    setIsSending(true);
    const optimisticUserMessage: ChatMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content: message,
      citations: [],
    };
    setMessages((current) => [...current, optimisticUserMessage]);

    try {
      const response = await sendChatMessage(sessionId, { message });
      setMessages(response.session.messages);
    } catch (caughtError) {
      const errorMessage = caughtError instanceof Error ? caughtError.message : "问答接口请求失败";
      setError(errorMessage);
    } finally {
      setIsSending(false);
    }
  }

  return (
    <main className="app-shell">
      <header className="top-bar">
        <div className="brand">
          <h1>Knowledge Platform</h1>
          <span>阿里云官方文档 RAG 问答</span>
        </div>
        <div className="status-pill">Session {sessionId.slice(0, 8)}</div>
      </header>

      <section className="workspace">
        <div className="conversation" aria-live="polite">
          {messages.length === 0 ? (
            <div className="empty-state">先采集并索引阿里云官方文档，再在这里进行多轮问答。</div>
          ) : (
            <div className="messages">
              {messages.map((message) => (
                <article className={`message ${message.role}`} key={message.id}>
                  <strong>{message.role === "user" ? "你" : `助手${message.intent ? ` · ${message.intent}` : ""}`}</strong>
                  <p>{message.content}</p>
                  {message.citations.length > 0 ? (
                    <ul className="citations">
                      {message.citations.map((citation) => (
                        <li key={`${message.id}-${citation.url}`}>
                          <a href={citation.url} rel="noreferrer" target="_blank">
                            {citation.title}
                          </a>
                          <span>{citation.source}</span>
                        </li>
                      ))}
                    </ul>
                  ) : null}
                </article>
              ))}
            </div>
          )}
        </div>

        <form className="composer" onSubmit={handleSubmit}>
          <textarea
            aria-label="客服消息"
            placeholder="输入关于阿里云官方文档的问题"
            value={input}
            onChange={(event) => setInput(event.target.value)}
          />
          <div className="composer-actions">
            <div className="error-text" role="alert">
              {error}
            </div>
            <button className="send-button" disabled={isSending || input.trim().length === 0} type="submit">
              {isSending ? "发送中" : "发送"}
            </button>
          </div>
        </form>
      </section>
    </main>
  );
}

export default App;
