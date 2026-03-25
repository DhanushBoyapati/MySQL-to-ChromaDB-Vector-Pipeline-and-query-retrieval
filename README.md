# 🧠 MySQL → ChromaDB Semantic Retrieval Pipeline

> **Transform structured relational data into a semantic vector database for intelligent, SQL-free querying — a core building block of enterprise RAG systems.**

---

## 📌 Overview

This project demonstrates how to bridge the gap between traditional relational databases and modern AI-powered retrieval. It extracts employee records from **MySQL**, converts them into natural-language documents, generates embeddings using **SentenceTransformers**, and stores them in **ChromaDB** — enabling semantic search without writing a single SQL query.

**Example query that just works:**
```
"Find AI engineers with deep learning experience"
```

---

## 🏗️ Architecture

```
MySQL Database (employees table)
        │
        ▼
Structured Row Extraction (Python)
        │
        ▼
Text Conversion → Semantic Documents
        │
        ▼
Embedding Generation (SentenceTransformers · all-MiniLM-L6-v2)
        │
        ▼
Persistent Vector Storage (ChromaDB)
        │
        ▼
Semantic Search + Metadata Filtering
```

---

## 📁 Project Structure

```
mysql-to-chromadb-rag-pipeline/
│
├── mysql_to_chroma.py       # MySQL → embedding → ChromaDB ingestion pipeline
├── query_chroma.py          # Semantic search query interface
├── employees_table.sql      # Database schema + sample dataset
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Relational DB | MySQL |
| Vector DB | ChromaDB |
| Embeddings | SentenceTransformers (`all-MiniLM-L6-v2`) |

---

## ✨ Features

- ✅ Extract structured employee data from MySQL
- ✅ Convert relational rows into semantic text documents
- ✅ Generate dense vector embeddings via SentenceTransformers
- ✅ Persist vectors in ChromaDB local storage
- ✅ Semantic similarity search across employee records
- ✅ Metadata-based filtering (department, role, experience)
- ✅ Modular ingestion and retrieval pipeline scripts

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/mysql-to-chromadb-rag-pipeline.git
cd mysql-to-chromadb-rag-pipeline
```

### 2. Install Dependencies

```bash
pip install mysql-connector-python chromadb sentence-transformers
```

### 3. Set Up the Database

Open MySQL and run:

```bash
SOURCE employees_table.sql;
```

This creates:
```
company_db
└── employees (table with sample records)
```

### 4. Run the Ingestion Pipeline

```bash
python mysql_to_chroma.py
```

**Expected output:**
```
STEP 1 COMPLETE: Data extracted successfully
STEP 2 COMPLETE: Documents created
STEP 3 COMPLETE: Embeddings generated
STEP 4 COMPLETE: Persistent vector storage ready
```

This generates a `chroma_storage/` directory containing your vector embeddings.

### 5. Run Semantic Search

```bash
python query_chroma.py
```

---

## 🔍 Example Queries

### Skill-Based
```
Who knows deep learning?
Find employees skilled in Kubernetes
Show people working with React
```

### Department-Based
```
Show employees in AI department
List Backend engineers
Find Cloud team members
```

### Hybrid Semantic + Metadata
```
Find AI engineers with Python experience
Show backend developers working with databases
Who in cloud team knows Docker?
```

---

## 📊 Example Output

```
Query: Who has deep learning experience?

Results:
──────────────────────────────────────────────────────
Employee Rahul Sharma works in AI department as ML Engineer...
Employee Kiran Kumar works in AI department as Computer Vision Engineer...
```

> Unlike SQL keyword matching, retrieval is powered by **semantic similarity** — capturing meaning, not just exact words.

---

## 🌐 Real-World Use Cases

This pipeline mirrors components used in production systems such as:

- 🏢 Enterprise knowledge assistants
- 👥 HR recommendation & talent search systems
- 🤖 Internal developer copilots
- 🎧 Customer-support automation platforms
- 🗃️ Structured database-aware chatbots
- 🔗 Retrieval-Augmented Generation (RAG) systems

**Production scenario example:**
```
User:   "Find backend engineers with API experience"
System: Retrieves semantically relevant candidates — no SQL needed.
```

---



## 🎓 Key Learning Outcomes

- Integrated MySQL with ChromaDB vector storage
- Enabled hybrid metadata + semantic retrieval
- Designed modular ingestion and query workflows for AI assistants

---

## 📬 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---
