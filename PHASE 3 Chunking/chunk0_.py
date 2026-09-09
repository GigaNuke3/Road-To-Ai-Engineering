def chunk_text(text, chunk_size=50):
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    
    return chunks
    

text = "a b c d e f g h i j k l m n o p q r s t u v w x y z"   # 26 words
chunks = chunk_text(text, chunk_size=5)
print(len(chunks)) 

for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk}")