from nltk.tokenize import sent_tokenize
from src.models import Document, Chunk
from src.chunkers import Chunker

# Splits text by sentences: NLTK provides sent_tokenize, which handles many abbreviations and punctuation patterns.
class SentenceChunker(Chunker):
      
      def chunk(self, document: Document) -> list[Chunk]:
        chunks = []
        doc_chunks = sent_tokenize(document.text, language='portuguese')
        for i, chunk_text in enumerate(doc_chunks):
                chunk_metadata = {**document.metadata, "chunk_index": i}
                chunks.append(Chunk(text=chunk_text, metadata=chunk_metadata))
        return chunks
  