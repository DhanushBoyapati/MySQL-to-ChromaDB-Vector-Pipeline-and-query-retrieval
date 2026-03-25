# STEP 1 — Import libraries
import mysql.connector
from sentence_transformers import SentenceTransformer
import chromadb


print("STEP 1: Connecting to MySQL database...\n")


# STEP 2 — Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # change if different
    password="you_password",      # change if different
    database="company_db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT name, department, role, experience, skills
FROM employees
""")

rows = cursor.fetchall()

print("Fetched rows from MySQL:\n")
for row in rows:
    print(row)


print("\n--------------------------------------------------")
print("STEP 2 COMPLETE: Data extracted successfully\n")


# STEP 3 — Convert rows into documents
documents = [
    f"Employee {row[0]} works in {row[1]} department as a {row[2]} with {row[3]} years experience. Skills: {row[4]}"
    for row in rows
]

print("Converted Documents:\n")
for doc in documents:
    print(doc)


print("\n--------------------------------------------------")
print("STEP 3 COMPLETE: Documents created\n")


# STEP 4 — Generate embeddings
print("Generating embeddings...\n")

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(documents)

print("Total embeddings created:", len(embeddings))


print("\n--------------------------------------------------")
print("STEP 4 COMPLETE: Embeddings generated\n")


# STEP 5 — Store embeddings inside persistent ChromaDB
print("Storing data into ChromaDB...\n")

client = chromadb.PersistentClient(path="./chroma_storage")

collection = client.get_or_create_collection(name="employees")


# Prepare metadata for filtering
metadata = [
    {
        "department": row[1],
        "role": row[2],
        "experience": row[3]
    }
    for row in rows
]


collection.add(
    documents=documents,
    embeddings=embeddings.tolist(),
    metadatas=metadata,
    ids=[str(i) for i in range(len(documents))]
)

print("Data stored successfully in ChromaDB")

print("Total stored records:", collection.count())


print("\n--------------------------------------------------")
print("STEP 5 COMPLETE: Persistent vector storage ready\n")


# # STEP 6 — Semantic search
# print("Running semantic search...\n")

# query = "Find employees skilled in Kubernetes?"

# query_embedding = model.encode([query])

# results = collection.query(
#     query_embeddings=query_embedding.tolist(),
#     n_results=2
# )

# print("Semantic Search Results:\n")

# for result in results["documents"][0]:
#     print(result)


# print("\n--------------------------------------------------")
# print("STEP 6 COMPLETE: Semantic search working\n")


# # STEP 7 — Metadata filtering example
# print("Running filtered search (AI department only)...\n")

# filtered_results = collection.query(
#     query_embeddings=query_embedding.tolist(),
#     n_results=2,
#     where={"department": "Kubernetes"}
# )

# print("Filtered Results:\n")

# for result in filtered_results["documents"][0]:
#     print(result)


# print("\n--------------------------------------------------")
# print("PROJECT COMPLETED SUCCESSFULLY 🚀")