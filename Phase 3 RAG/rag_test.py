import chromadb

client = chromadb.Client()

collection = client.create_collection(name="my_documents")

collection.add(
    documents=[
        "How do I reset my password?",
        "Steps to recover your account access",
        "What's the best pizza topping?"
    ],
    ids=["doc1", "doc2", "doc3"]
)

results = collection.query(
    query_texts=["I forgot my login credentials, help"],
    n_results=2
)

print(results)