from knowledge_platform.datasources.base import DataSource, SourceDocument


class MemoryDataSource(DataSource):
    def __init__(self, documents: list[SourceDocument] | None = None) -> None:
        self._documents = documents or []

    def search(self, query: str, limit: int = 5) -> list[SourceDocument]:
        normalized_query = query.strip().lower()
        if not normalized_query:
            return []

        matches = [
            document
            for document in self._documents
            if normalized_query in document.title.lower() or normalized_query in document.content.lower()
        ]
        return matches[:limit]
