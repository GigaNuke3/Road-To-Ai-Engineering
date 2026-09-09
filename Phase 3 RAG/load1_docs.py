import os
import chromadb
import requests

def load_documents(folder_path):
    documents = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r") as file:
                content = file.read()
                documents.append(content)
                filenames.append(filename)
    return documents, filenames

docs, names = load_documents("docs")

client = chromadb.PersistentClient(path="./chroma_db_projects")
collection = client.get_or_create_collection(name="my_projects")

collection.add(
    documents=docs,
    ids=names
)

query = "Which project is a desktop application?"

results = collection.query(query_texts=[query], n_results=2)
retrieved_docs = results["documents"][0]

print("RETRIEVED DOCUMENTS:")
for doc in retrieved_docs:
    print("-", doc)
print("---")

context = "\n".join(retrieved_docs)

prompt = f"""Answer the question using ONLY the context below. List only the PROJECT NAMES (not other tools or products mentioned) that are desktop applications.
"

Context:
{context}

Question: {query}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3.2:3b", "prompt": prompt, "stream": False}
)

print(response.json()["response"])