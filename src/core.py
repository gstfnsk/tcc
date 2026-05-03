from models import RetrievalResult
from src.chunkers import Chunker
from src.chunkers.simple_fixed_recursive_chunker import SimpleChunker
from src.embedders.all_minilm import AllMinilmEmbedder
from src.store.chroma import ChromaStore
from loader import load_documents

class Pipeline:
    def __init__(self, chunker: SimpleChunker,
                 embedder: AllMinilmEmbedder, store: ChromaStore):
        self.chunker = chunker
        self.embedder = embedder
        self.store = store

    def ingest(self, source: str) -> int:
        documents = load_documents(source)
        all_chunks = []
        for doc in documents:
            chunks = self.chunker.chunk(doc)
            all_chunks.extend(chunks)
        texts = [chunk.text for chunk in all_chunks]
        embeddings = self.embedder.embed(texts)
        assert len(embeddings) == len(all_chunks)
        self.store.add(all_chunks, embeddings)
        return len(all_chunks)

    # for now, we're just querying the store directly
    def retrieve(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        query_embedding = self.embedder.embed_query(query)
        return self.store.query(query_embedding, top_k)