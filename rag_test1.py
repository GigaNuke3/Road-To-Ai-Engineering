import chromadb
import requests

client = chromadb.PersistentClient(path=",/chroma_db")
collection = client.create_collection(name="my_documents")

collection.add(
    documents=[
        "How do I reset my password? Go to Settings > Security > Reset Password.",
        "Steps to recover your account access: contact support with your registered email.",
        "What's the best pizza topping? Pepperoni is the most popular choice."
    ],
    ids=["doc1", "doc2", "doc3"]
)

query = "I forgot my login credentials, help"

results = collection.query(query_texts=[query], n_results=2)
retrieved_docs = results["documents"][0]   # extract just the document texts

context = "\n".join(retrieved_docs)   # combine retrieved docs into one block of text

prompt = f"""Answer the question using ONLY the context below. If the context doesn't contain the answer, say "I don't know."

Context:
{context}

Question: {query}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3.2:3b", "prompt": prompt, "stream": False}
)

print(response.json()["response"])