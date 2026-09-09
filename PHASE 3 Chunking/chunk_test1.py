def chunk_text(text, chunk_size=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

with open("docs/callama.txt") as f1, open("docs/kaizen.txt") as f2, open("docs/elib.txt") as f3:
    long_text = f1.read() + " " + f2.read() + " " + f3.read()

chunks = chunk_text(long_text, chunk_size=10)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk}")