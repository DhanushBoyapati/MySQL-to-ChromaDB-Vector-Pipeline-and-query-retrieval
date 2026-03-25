import chromadb
from sentence_transformers import SentenceTransformer


print("Loading ChromaDB collection...\n")

# Load persistent ChromaDB storage
client = chromadb.PersistentClient(path="./chroma_storage")

collection = client.get_collection(name="employees")


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Example query
query = "Who works in cybersecurity?"

query_embedding = model.encode([query])


# Perform semantic search
results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=3
)


print("Search Results:\n")

for doc in results["documents"][0]:
    print(doc)




    

# STEP 7 — Metadata filtering example
print("Running filtered search (AI department only)...\n")

filtered_results = collection.query(
    query_embeddings=query_embedding.tolist(),
    n_results=2,
    where={"experience": {"$gte": 4}}
)

print("Filtered Results:\n")

for result in filtered_results["documents"][0]:
    print(result)


print("\n--------------------------------------------------")
print("PROJECT COMPLETED SUCCESSFULLY 🚀")