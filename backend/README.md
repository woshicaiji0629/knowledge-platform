# Knowledge Platform Backend

Python + FastAPI backend for the RAG knowledge platform.

Use `uv` to manage the backend environment:

```bash
uv sync --extra dev
uv run uvicorn knowledge_platform.main:app --reload
```
