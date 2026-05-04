import ollama
from src.embedders import Embedder

class GemmaEmbedder(Embedder):
        
    def embed(self, texts: list[str])-> list[list[float]]:
        response = ollama.embed(
        model="gemma",
        input=texts
    )
        return response["embeddings"]
    
    def embed_query(self, query: str) -> list[float]:
        return self.embed([query])[0]

