from abc import ABC, abstractmethod

class Generator(ABC):
    @abstractmethod
    def generate(self, query: str, retrieved_chunks: list[str]) -> str:
        pass