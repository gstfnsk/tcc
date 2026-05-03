from abc import ABC, abstractmethod
from src.models import Chunk, RetrievalResult

class VectorStore(ABC):
    @abstractmethod
    def add(self, chunks: list[Chunk], embeddings: list[list[float]]):
        pass

    @abstractmethod
    def query(self, query_embedding: list[float], top_k: int) -> list[RetrievalResult]:
        pass