import asyncio
import json
import urllib.error
import urllib.parse
import urllib.request
import uuid
from dataclasses import asdict, dataclass
from typing import Any, cast


@dataclass(frozen=True)
class VectorPoint:
    id: str
    vector: list[float]
    payload: dict[str, Any]


@dataclass(frozen=True)
class ScoredVectorPoint:
    id: str
    score: float
    payload: dict[str, Any]


@dataclass(frozen=True)
class QdrantConfig:
    endpoint: str = "http://localhost:6333"
    collection_name: str = "aliyun_docs_product_v1"
    distance: str = "Cosine"
    timeout_seconds: float = 30.0


class QdrantVectorStore:
    def __init__(self, config: QdrantConfig) -> None:
        self._config = config

    async def ensure_collection(self, vector_size: int) -> None:
        if vector_size <= 0:
            raise ValueError("vector_size must be greater than 0")
        await asyncio.to_thread(self._ensure_collection_sync, vector_size)

    async def upsert_points(self, points: list[VectorPoint]) -> int:
        if not points:
            return 0
        await asyncio.to_thread(self._upsert_points_sync, points)
        return len(points)

    async def existing_source_ids(self, source_ids: list[str]) -> set[str]:
        if not source_ids:
            return set()
        return await asyncio.to_thread(self._existing_source_ids_sync, source_ids)

    async def search_points(self, vector: list[float], limit: int = 5) -> list[ScoredVectorPoint]:
        if not vector:
            return []
        if limit <= 0:
            raise ValueError("limit must be greater than 0")
        return await asyncio.to_thread(self._search_points_sync, vector, limit)

    def _ensure_collection_sync(self, vector_size: int) -> None:
        payload = {
            "vectors": {
                "size": vector_size,
                "distance": self._config.distance,
            }
        }
        self._request_json(
            method="PUT",
            path=f"/collections/{urllib.parse.quote(self._config.collection_name)}",
            payload=payload,
        )

    def _upsert_points_sync(self, points: list[VectorPoint]) -> None:
        payload = {
            "points": [
                {
                    "id": _qdrant_point_id(point.id),
                    "vector": point.vector,
                    "payload": {"source_id": point.id, **point.payload},
                }
                for point in points
            ]
        }
        self._request_json(
            method="PUT",
            path=f"/collections/{urllib.parse.quote(self._config.collection_name)}/points?wait=true",
            payload=payload,
        )

    def _existing_source_ids_sync(self, source_ids: list[str]) -> set[str]:
        payload = {
            "ids": [qdrant_point_id(source_id) for source_id in source_ids],
            "with_payload": True,
            "with_vector": False,
        }
        try:
            response_data = self._request_json(
                method="POST",
                path=f"/collections/{urllib.parse.quote(self._config.collection_name)}/points",
                payload=payload,
            )
        except RuntimeError as error:
            if "HTTP 404" in str(error):
                return set()
            raise

        result = response_data.get("result")
        if not isinstance(result, list):
            return set()

        existing_source_ids: set[str] = set()
        for item in cast(list[object], result):
            if not isinstance(item, dict):
                continue
            point = cast(dict[object, object], item)
            payload_data = point.get("payload")
            if not isinstance(payload_data, dict):
                continue
            source_id = cast(dict[object, object], payload_data).get("source_id")
            if isinstance(source_id, str):
                existing_source_ids.add(source_id)
        return existing_source_ids

    def _search_points_sync(self, vector: list[float], limit: int) -> list[ScoredVectorPoint]:
        payload = {
            "vector": vector,
            "limit": limit,
            "with_payload": True,
            "with_vector": False,
        }
        response_data = self._request_json(
            method="POST",
            path=f"/collections/{urllib.parse.quote(self._config.collection_name)}/points/search",
            payload=payload,
        )
        result = response_data.get("result")
        if not isinstance(result, list):
            return []

        points: list[ScoredVectorPoint] = []
        for item in cast(list[object], result):
            if not isinstance(item, dict):
                continue
            point = cast(dict[object, object], item)
            point_id = point.get("id")
            score = point.get("score")
            payload_data = point.get("payload")
            if (
                not isinstance(point_id, str)
                or not isinstance(score, int | float)
                or not isinstance(payload_data, dict)
            ):
                continue
            points.append(
                ScoredVectorPoint(
                    id=point_id,
                    score=float(score),
                    payload=cast(dict[str, Any], payload_data),
                )
            )
        return points

    def _request_json(self, method: str, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            f"{self._config.endpoint.rstrip('/')}{path}",
            data=body,
            headers={"Content-Type": "application/json"},
            method=method,
        )
        try:
            with urllib.request.urlopen(request, timeout=self._config.timeout_seconds) as response:
                response_body = response.read().decode("utf-8")
        except urllib.error.HTTPError as error:
            body_text = error.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Qdrant request failed: HTTP {error.code}: {body_text}") from error
        except urllib.error.URLError as error:
            raise RuntimeError(f"Qdrant request failed: {error.reason}") from error

        if not response_body:
            return {}
        response_data = json.loads(response_body)
        if not isinstance(response_data, dict):
            raise RuntimeError("Qdrant response is not a JSON object")
        return cast(dict[str, Any], response_data)


def vector_point_from_record(record: dict[str, Any], vector: list[float], content: str) -> VectorPoint:
    payload = dict(record)
    payload["content"] = content
    return VectorPoint(
        id=str(record["id"]),
        vector=vector,
        payload=payload,
    )


def vector_point_to_dict(point: VectorPoint) -> dict[str, Any]:
    return asdict(point)


def _qdrant_point_id(source_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, source_id))


def qdrant_point_id(source_id: str) -> str:
    return _qdrant_point_id(source_id)
