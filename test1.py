from sentence_transformers import SentenceTransformer
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

model= SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "How do I reset my password", 
    "Steps to recover your account access", 
    "What's the best pizza topping"
]
embeddings = model.encode(sentences)

for sentence, embedding in zip (sentences, embeddings):
    print(sentence, "->", embedding[:5], "...")

print(cosine_similarity(embeddings[0], embeddings[1]))
print(cosine_similarity(embeddings[0], embeddings[2]))