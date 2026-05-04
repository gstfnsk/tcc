from src.core import Pipeline
from src.chunkers.simple_fixed_recursive_chunker import SimpleChunker
from src.embedders.all_minilm import AllMinilmEmbedder
from src.store.chroma import ChromaStore

pipeline = Pipeline(
    chunker=SimpleChunker(chunk_size=300, chunk_overlap=50),
    embedder=AllMinilmEmbedder(),
    store=ChromaStore(path="./chroma_db", collection_name="test")
)

query = "quais as doenças da mandioca?"

ingested_count = pipeline.ingest("./data/q_and_a_formatted.json")
results = pipeline.retrieve(query, top_k=20)

for r in results:
    print("----")
    print(r.chunk.text)
    print(r.score)