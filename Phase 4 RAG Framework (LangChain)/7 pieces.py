from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# LOADING - replaces your manual PdfReader loop
loader = PyPDFLoader("ELIB-FINAL-MANUSCRIPT.pdf")
pages =loader.load()

print("Total pages loaded:", len(pages))
print(pages[12].page_content[:300]) #preview page 12, same you targeted manually before

#CHUNKING - replaces your manual chunk_by_setneces function
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, # roughly, characters per chunk (not exactly words/sentences like before)
    chunk_overlap=50      # NEW concept — chunks slightly overlap each other
)

chunks = splitter.split_documents(pages[12:20])   # same page range you used manually

print("Total chunks:", len(chunks))
print(chunks[0].page_content)


from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

# EMBEDDINGS — replaces your manual sentence-transformers usage
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# VECTOR STORE — replaces your manual chromadb.PersistentClient setup
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_langchain_db"
)

# RETRIEVAL — replaces your manual collection.query()
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
print("Total documents in vectorstore:", vectorstore._collection.count())

query = "What problem does E-LIB solve?"
retrieved_docs = retriever.invoke(query)

for doc in retrieved_docs:
    print("-", doc.page_content[:150], "...")

# GENERATION — replaces your manual requests.post() call to Ollama
llm = OllamaLLM(model="llama3.2:3b")
context = "\n".join([doc.page_content for doc in retrieved_docs])

from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template("""Answer the question using ONLY the context below. If the context doesn't contain the answer, say "I don't know."

Context:
{context}

Question: {question}
""")

prompt = template.format(context=context, question=query)
print(prompt)

response = llm.invoke(prompt)
print(response)