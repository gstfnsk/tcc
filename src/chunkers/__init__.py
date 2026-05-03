from abc import ABC, abstractmethod
from src.models import Chunk, Document
class Chunker(ABC):
    @abstractmethod
    def chunk(self, document: Document) -> list[Chunk]:
        pass