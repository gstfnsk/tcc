from dataclasses import dataclass

@dataclass
class Document:
    text: str
    metadata: dict

@dataclass
class Chunk:
    text: str
    metadata: dict 

@dataclass
class RetrievalResult:
    chunk: Chunk
    score: float