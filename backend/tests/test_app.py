from typing import Any, cast

from fastapi.testclient import TestClient

from knowledge_platform.main import app

client = cast(Any, TestClient(app))


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_customer_service_requires_aliyun_configuration() -> None:
    response = client.post(
        "/api/v1/customer-service/chat",
        json={"message": "hello", "session_id": "demo"},
    )

    assert response.status_code == 503
    assert "Aliyun customer service provider is not configured" in response.json()["detail"]
