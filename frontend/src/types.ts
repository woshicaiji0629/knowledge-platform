export interface SendMessageRequest {
  message: string;
}

export interface Citation {
  title: string;
  url: string;
  source: string;
  score: number;
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  created_at?: string;
  citations: Citation[];
  intent?: string;
}

export interface ChatSession {
  id: string;
  title: string;
  created_at: string;
  updated_at: string;
  messages: ChatMessage[];
}

export interface SendMessageResponse {
  session: ChatSession;
  message: ChatMessage;
}
