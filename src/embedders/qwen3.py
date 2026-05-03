# models for embedding
import ollama
from src.embedders import Embedder  


class Qwen3Embedder(Embedder):
    
    def embed(self):
        response = ollama.embed(
            model="qwen3",
            input=self.text
        )
        return response.embeddings

