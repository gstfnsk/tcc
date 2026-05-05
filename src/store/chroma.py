import chromadb
import uuid
from src.store import VectorStore
from src.models import RetrievalResult, Chunk

class ChromaStore(VectorStore):

    def __init__(self, path: str = "./chroma_db", collection_name: str = "default"):
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection(collection_name)

    def add(self, chunks: list[Chunk], embeddings: list[list[float]])-> None:
        assert len(chunks) == len(embeddings)
        ids = [str(uuid.uuid4()) for _ in chunks]       
        metadatas = [chunk.metadata for chunk in chunks]
        documents = [chunk.text for chunk in chunks] # for now storing the documents as well 
        self.collection.add(ids=ids, embeddings=embeddings, metadatas=metadatas, documents=documents)

    def query(self, query_embedding: list[float], top_k: int)->list[RetrievalResult]:
        results = self.collection.query(query_embeddings=[query_embedding], n_results=top_k)
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]
        output = []
        for doc, meta, dist in zip(documents, metadatas, distances):
            score = 1 / (1 + dist)  # convert distance to a similarity score
            output.append(RetrievalResult(chunk=Chunk(text=doc, metadata=meta), score=score))
        return output