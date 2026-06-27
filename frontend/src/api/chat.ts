import type { SendMessageRequest, SendMessageResponse } from "../types";

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";

export async function sendChatMessage(sessionId: string, request: SendMessageRequest): Promise<SendMessageResponse> {
  const response = await fetch(`${apiBaseUrl}/api/v1/chat/sessions/${sessionId}/messages`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(request),
  });

  if (!response.ok) {
    const errorBody = (await response.json().catch(() => null)) as { detail?: string } | null;
    throw new Error(errorBody?.detail ?? "问答接口请求失败");
  }

  return response.json() as Promise<SendMessageResponse>;
}
