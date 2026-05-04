from core import Pipeline
from chunkers.simple_fixed_recursive_chunker import FixedChunker
from embedders.all_minilm import AllMinilmEmbedder
from store.chroma import ChromaStore

pipeline = Pipeline(
    chunker=FixedChunker(chunk_size=1000, chunk_overlap=200),
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