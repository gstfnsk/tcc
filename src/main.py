from src.core import Pipeline
from src.chunkers.simple_fixed_recursive_chunker import SimpleChunker
from src.embedders.nomic_moe import NomicEmbedder
# from src.embedders.all_minilm import AllMinilmEmbedder
from src.store.chroma import ChromaStore
from src.generator.oss_generator import gpt_oss_Generator

pipeline = Pipeline(
    chunker=SimpleChunker(chunk_size=300, chunk_overlap=50),
    embedder=NomicEmbedder(),
    store=ChromaStore(path="./chroma_db", collection_name="test"), 
    generator=gpt_oss_Generator()
)

# ingested_count = pipeline.ingest("./data/q_and_a_formatted.json")

print("Digite a pergunta:")
query = input()
retrieved_chunks = pipeline.retrieve(query, top_k=3)
generation = pipeline.generate_answer(query, retrieved_chunks=retrieved_chunks)

# for r in retrieved_chunks:
#     print("----")
#     print(r.chunk.text)
#     print(r.score)

# print("Resposta crua gerada:")
# print(generation)

print("Resposta final:")
print(generation.message.content)
