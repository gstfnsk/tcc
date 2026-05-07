#NOTE: top embedder model choice

import ollama
from src.embedders import Embedder

class NomicEmbedder(Embedder):
        
    def embed(self, texts: list[str])-> list[list[float]]:
        response = ollama.embed(
        model="nomic-embed-text-v2-moe",
        input=texts
    )
        return response["embeddings"]
    
    def embed_query(self, query: str) -> list[float]:
        return self.embed([query])[0]

