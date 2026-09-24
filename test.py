from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("ELIB-FINAL-MANUSCRIPT.pdf")
pages = loader.load()

print("Total pages loaded:", len(pages))
print(pages[12].page_content[:300])

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(pages[12:20])

print("Total chunks:", len(chunks))
print(chunks[0].page_content)

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_langchain_db"
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
print("Total documents in vectorstore:", vectorstore._collection.count())

query = "What problem does E-LIB solve?"
retrieved_docs = retriever.invoke(query)

for doc in retrieved_docs:
    print("-", doc.page_content[:150], "...")

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


# ============================================
# NEW — CHAIN VERSION (added below, doesn't replace anything above)
# ============================================
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def format_docs(docs):
    return "\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | template
    | llm
    | StrOutputParser()
)

query2 = "What is the scope of E-LIB?"

response2 = rag_chain.invoke(query2)
print("CHAIN RESPONSE:")
print(response2)

