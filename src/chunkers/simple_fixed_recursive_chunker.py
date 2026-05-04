from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.models import Document, Chunk
from src.chunkers import Chunker

# Splits text hierarchically (sections → paragraphs) to preserve logical structure.
class SimpleChunker(Chunker):
      def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
      
      def chunk(self, document: Document) -> list[Chunk]:
        splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        chunks = []
        doc_chunks = splitter.split_text(document.text)
        for i, chunk_text in enumerate(doc_chunks):
                chunk_metadata = {**document.metadata, "chunk_index": i}
                chunks.append(Chunk(text=chunk_text, metadata=chunk_metadata))
        return chunks
        