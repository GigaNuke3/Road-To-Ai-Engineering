def chunk_text(text, chunk_size=10):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

with open("docs/callama.txt") as f:
    callama_chunks = chunk_text(f.read())

with open("docs/kaizen.txt") as f:
    kaizen_chunks = chunk_text(f.read())

with open("docs/elib.txt") as f:
    elib_chunks = chunk_text(f.read())

print("Callama chunks:", callama_chunks)
print("Kaizen chunks:", kaizen_chunks)
print("Elib chunks:", elib_chunks)