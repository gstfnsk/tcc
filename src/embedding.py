# models for embedding
import ollama

def embed_text(text, model_name):
    response = ollama.embed(
        model=model_name,
        input=text
    )
    return response.embeddings

