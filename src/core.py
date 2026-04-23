# Document, Chunk, RetrievalResult, Pipeline

from dataclasses import dataclass

@dataclass
class Document:
    text: str
    metadata: dict

@dataclass
class Chunk:
    text: str
    metadata: dict    # inherits from Document metadata + chunk_index

@dataclass
class RetrievalResult:
    chunk: Chunk
    score: float

class Pipeline:
    def __init__(self, loader: Loader, chunker: Chunker,
                 embedder: Embedder, store: VectorStore):
        self.loader = loader
        self.chunker = chunker
        self.embedder = embedder
        self.store = store

    def ingest(self, source: str) -> int:
        documents = self.loader.load(source)
        total = 0
        for doc in documents:
            chunks = self.chunker.chunk(doc.text, doc.metadata)
            embeddings = self.embedder.embed([c.text for c in chunks])
            self.store.add(chunks, embeddings)
            total += len(chunks)
        return total

    def retrieve(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        query_embedding = self.embedder.embed([query])[0]
        return self.store.query(query_embedding, top_k)