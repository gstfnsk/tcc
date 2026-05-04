import ollama
from src.embedders import Embedder

class Qwen3Embedder(Embedder):
        
    def embed(self, texts: list[str])-> list[list[float]]:
        response = ollama.embed(
        model="qwen3",
        input=texts
    )
        return response["embeddings"]
    
    def embed_query(self, query: str) -> list[float]:
        return self.embed([query])[0]

