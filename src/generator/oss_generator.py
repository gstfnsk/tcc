from ollama import chat
import ollama
from src.generator import Generator

class gpt_oss_Generator(Generator):
    def generate(self, query: str, retrieved_chunks: list[str]) -> str:
        context = "\n\n".join(retrieved_chunks)
        prompt = f"Contexto: {context}\n\nPergunta: {query}\nResposta:"
        content = "Você é um assistente útil que responde perguntas com base no contexto fornecido. Não use nenhuma informação que não esteja no contexto. Se você não souber a resposta, diga que não sabe. Sempre use toda a informação disponível do contexto para responder a pergunta."
        
        response = ollama.chat(
            model="gpt-oss",
            messages=[{"role": "system", "content": content},
                      {"role": "user", "content": prompt}]
        )
        print(response.message.content)
        return response
        
        # return response["choices"][0]["message"]["content"].strip()
