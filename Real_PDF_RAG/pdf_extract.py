import re
import chromadb
import requests
from pypdf import PdfReader

def chunk_by_sentences(text, sentences_per_chunk=3):
    sentences =re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    for i in range(0, len(sentences), sentences_per_chunk):
        chunk = " ".join(sentences[i:i+sentences_per_chunk])
        chunks.append(chunk)
    return chunks

reader = PdfReader("ELIB-FINAL-MANUSCRIPT.pdf")

text=""
for page in reader.pages[12:20]:
    text += page.extract_text()
    

chunks = chunk_by_sentences(text, sentences_per_chunk=3)
ids=[f"elib_chunk{i}" for i in range(len(chunks))]

print("Total chunks:", len(chunks))

client = chromadb.PersistentClient(path="./chroma_db_pdf_v2")
collection = client.get_or_create_collection(name="elib_manuscript")

collection.add(documents=chunks, ids=ids)

query = "What is E-LIB?"

results = collection.query(query_texts=[query], n_results=2)
retrieved_docs = results["documents"][0]

print("RETRIEVED:")
for doc in retrieved_docs:
    print("-", doc)

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