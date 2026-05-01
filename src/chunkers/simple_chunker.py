from langchain_text_splitters import RecursiveCharacterTextSplitter
from core import Document, Chunk

class SimpleChunker:
      def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
      
      def chunk_documents(self, documents: list[Document]) -> list[Chunk]:
        pass
        
#converter p/ dataclass Chunk