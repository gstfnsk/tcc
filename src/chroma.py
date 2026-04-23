import chromadb

question_and_answer_collection_name = "question_and_answer_collection"
# quaesta_collection_name = "quaesta_collection"

question_and_answer_path = "./chroma_db/question_and_answer"
# quaesta_path = "./chroma_db/quaesta"

client = chromadb.PersistentClient(path=question_and_answer_path)

collection = client.create_collection(question_and_answer_collection_name)