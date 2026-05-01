# models for embedding
import ollama

class ModeloEmbedder:
    def __init__(self, text: list(str)):
        self.text = text
        
    def embed(self):
        response = ollama.embed(
            model="modelo",
            input=self.text
        )
        return response.embeddings

