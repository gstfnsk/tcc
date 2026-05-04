from langchain_text_splitters import TextSplitter
from src.models import Document, Chunk
from src.chunkers import Chunker

#Splits text into equal-sized chunks with overlaps to preserve context.

class FixedChunker(Chunker):
      def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
      
      def chunk(self, document: Document) -> list[Chunk]:
        splitter = TextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        chunks = []
        doc_chunks = splitter.split_text(document.text)
        for i, chunk_text in enumerate(doc_chunks):
                chunk_metadata = {**document.metadata, "chunk_index": i}
                chunks.append(Chunk(text=chunk_text, metadata=chunk_metadata))

        return chunks