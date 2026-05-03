# models for embedding
import ollama
from src.embedders import Embedder  


class GemmaEmbedder(Embedder):
        
    def embed(self):
        response = ollama.embed(
            model="gemma",
            input=self.text
        )
        return response.embeddings