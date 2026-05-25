from src.models import Document, Chunk
from src.chunkers import Chunker

# Splits text by paragraphs.
class ParagraphChunker(Chunker):
      
      def chunk(self, document: Document) -> list[Chunk]:
        paragraphs = [
            p.strip()
            for p in document.text.split("\n\n")
            if p.strip()
        ]
        chunks = []
        for i, paragraph in enumerate(paragraphs):
                chunk_metadata = {**document.metadata, "chunk_index": i}
                chunks.append(Chunk(text=paragraph, metadata=chunk_metadata))
        return chunks
  