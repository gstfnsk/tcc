import json
import time 
import os
from core import Document

def load_documents() -> list[Document]:
    path = "../data/todos_livros_separados_por_livro.json"

    # variable to measure the time to process the documents
    # start_time = time.time()

    with open(path, "r", encoding="utf-8") as file:
        corpus = json.load(file)

    documents = []

    # for each book, creates a document with text: question+answer and metadata: book_name+year+question
    for book_name, book_data in corpus:
        year = book_data["ano_publicacao"]
        for qa in book_data["p_e_r"]:
            question = qa["pergunta"]
            answer = qa["resposta"]
            text = question + " " + answer
            metadata = {
                "book_name": book_name,
                "year": year,
                "question": question
            }
            document = Document(text=text, metadata=metadata)
            # add document to the list of documents
            documents.append(document)

    return documents