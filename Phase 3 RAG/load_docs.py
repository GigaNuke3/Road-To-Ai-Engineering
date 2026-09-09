import os

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
for name, content in zip(names, docs):
    print(f"{name}: {content[:50]}...")