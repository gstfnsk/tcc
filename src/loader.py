import json
import time 
import os
from src.models import Document

def load_documents(source_path: str) -> list[Document]:

    # variable to measure the time to process the documents
    start_time = time.time()

    with open(source_path, "r", encoding="utf-8") as file:
        corpus = json.load(file)

    documents = []

    # for each book in the corpus, we create a document for each question-answer pair, with metadata containing the book name, year and question
    for book_name, book_data in corpus.items():
        year = book_data["ano_publicacao"]

        for qa in book_data["p_e_r"]:
            question = qa["pergunta"]
            answer = qa["resposta"]

            text = f"{question} {answer}"
            metadata = {
                "book_name": book_name,
                "year": year,
                "question": question
            }

            documents.append(Document(text=text, metadata=metadata))

    print(f"Loaded {len(documents)} documents from {source_path}")

    end_time = time.time()
    print(f"Time taken to load documents: {end_time - start_time:.2f} seconds")

    return documents
