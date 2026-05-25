from src.core import Pipeline
from src.chunkers.paragraph_chunker import ParagraphChunker
from src.embedders.nomic_moe import NomicEmbedder
# from src.embedders.all_minilm import AllMinilmEmbedder
from src.store.chroma import ChromaStore
from src.generator.oss_generator import gpt_oss_Generator
import time

pipeline = Pipeline(
    chunker=ParagraphChunker(),
    embedder=NomicEmbedder(),
    store=ChromaStore(path="./chroma_db", collection_name="test"), 
    generator=gpt_oss_Generator()
)

# ingestion_start_time = time.time()
# ingested_count = pipeline.ingest("./data/q_and_a_formatted.json")
# ingestion_end_time = time.time()
# print(f"Ingested {ingested_count} chunks in {ingestion_end_time - ingestion_start_time:.2f} seconds.")

print("Digite a pergunta:")
query = input()
retrieval_start_time = time.time()
retrieved_chunks = pipeline.retrieve(query, top_k=3)
retrieval_end_time = time.time()
print(f"Retrieved {len(retrieved_chunks)} chunks in {retrieval_end_time - retrieval_start_time:.2f} seconds.")

generation_start_time = time.time()
generation = pipeline.generate_answer(query, retrieved_chunks=retrieved_chunks)
generation_end_time = time.time()
print(f"Generated answer in {generation_end_time - generation_start_time:.2f} seconds.")

# for r in retrieved_chunks:
#     print("----")
#     print(r.chunk.text)
#     print(r.score)

print("Resposta crua gerada:")
print(generation)

print("Resposta final:")
print(generation.message.content)
