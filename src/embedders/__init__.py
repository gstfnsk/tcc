from abc import ABC, abstractmethod
from models import Chunk

class Embedder(ABC):
    @abstractmethod
    def embed(self, texts: list[str]) -> list[list[float]]:
        pass

    def embed_query(self, query: str) -> list[float]:
        return self.embed([query])[0]