from ollama import chat
import ollama
from src.generator import Generator

class gpt_oss_Generator(Generator):
    def generate(self, query: str, retrieved_chunks: list[str]) -> str:
        context = "\n\n".join(retrieved_chunks)
        prompt = f"Contexto: {context}\n\nPergunta: {query}\nResposta:"
        content = "You are a helpful assistant that answers questions based on the provided context. Do not use any information that is not in the context. If you don't know the answer, say you don't know. Always use all available information from the context to answer the question."
        
        response = ollama.chat(
            model="gpt-oss",
            messages=[{"role": "system", "content": content},
                      {"role": "user", "content": prompt}]
        )
        print(response.message.content)
        return response
        
        # return response["choices"][0]["message"]["content"].strip()
