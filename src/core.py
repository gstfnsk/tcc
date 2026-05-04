from src.models import RetrievalResult
from src.chunkers.simple_fixed_recursive_chunker import SimpleChunker
from src.embedders.gemma import GemmaEmbedder
from src.store.chroma import ChromaStore
from src.loader import load_documents

class Pipeline:
    def __init__(self, chunker: SimpleChunker,
                 embedder: GemmaEmbedder, store: ChromaStore):
        self.chunker = chunker
        self.embedder = embedder
        self.store = store

    def ingest(self, source: str) -> int:
        documents = load_documents(source)
        all_chunks = []
        for doc in documents:
            chunks = self.chunker.chunk(doc)
            all_chunks.extend(chunks)

        batch_size = 5
        for i in range(0, len(all_chunks), batch_size):
            print(f"Processing batch {i//batch_size + 1}/{(len(all_chunks) + batch_size - 1)//batch_size}...")
            batch_chunks = all_chunks[i:i+batch_size]
            texts = [chunk.text for chunk in batch_chunks]
            print(f"Batch size: {len(texts)}, avg length: {sum(len(t) for t in texts)/len(texts)}")
            print("Max length:", max(len(t) for t in texts))
            embeddings = self.embedder.embed(texts)
            assert len(embeddings) == len(batch_chunks)
            self.store.add(batch_chunks, embeddings)
        return len(all_chunks)

    # for now, we're just querying the store directly
    def retrieve(self, query: str, top_k: int = 5) -> list[RetrievalResult]:
        query_embedding = self.embedder.embed_query(query)
        return self.store.query(query_embedding, top_k)