from typing import Any, List, Protocol


class VectorStore(Protocol):
    def similarity_search(self, query: str) -> List[Any]: ...
