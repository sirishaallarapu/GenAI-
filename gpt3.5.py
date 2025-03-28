from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
text = "Machine learning is transforming the world."
embedding = model.encode(text)
print("Embedding Shape:", embedding.shape)
print("Embedding Vector:", embedding)


