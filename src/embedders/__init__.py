from abc import ABC, abstractmethod

class Embedder(ABC):
    @abstractmethod
    def embed(self, texts: list[str]) -> list[list[float]]:
        pass

    @abstractmethod
    def embed_query(self, query: str) -> list[float]:
        pass