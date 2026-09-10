import os
import chromadb
import requests

def chunk_text(text, chunk_size=100):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def load_and_chunk_documents(folder_path):
    all_chunks = []
    all_ids = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r") as file:
                content = file.read()
                chunks = chunk_text(content, chunk_size=80)

                for i, chunk in enumerate(chunks):
                    all_chunks.append(chunk)
                    all_ids.append(f"{filename}_chunk{i}")

    return all_chunks, all_ids

chunks, ids = load_and_chunk_documents("docs")

print("Total chunks created:", len(chunks))
for chunk_id, chunk in zip(ids, chunks):
    print(chunk_id, "->", chunk)

client = chromadb.PersistentClient(path="./chroma_db_chunked")
collection = client.get_or_create_collection(name="chunked_projects")

collection.add(
    documents=chunks,
    ids=ids
)

query = "What does Kaizen do?"

results = collection.query(query_texts=[query], n_results=1)
retrieved_docs = results["documents"][0]

print("RETRIEVED:", retrieved_docs)

context = "\n".join(retrieved_docs)

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
