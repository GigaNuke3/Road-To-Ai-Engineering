def chunk_text(text, chunk_size=50):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    return chunks

long_text = "This is a test sentence. " * 30

chunks = chunk_text(long_text, chunk_size=10)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk}")

