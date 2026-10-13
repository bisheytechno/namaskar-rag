# Namaskar RAG

Learning Retrieval-Augmented Generation (RAG) using Python and ChromaDB — a step toward AI engineering.

---

## What This Covers

- Document indexing — store knowledge-base documents
- Text embeddings — convert text into numerical vectors
- Persistent storage — save data using ChromaDB
- Semantic search — retrieve relevant documents
- Distance inspection — analyze retrieval results
- RAG fundamentals — understand the retrieval stage

---

## Tech Stack

- Python 3.x
- ChromaDB
- sentence-transformers
- Hugging Face
- VS Code

---

## Project Structure

```text
namaskar-rag/
│
├── myvenv/                 → Virtual environment (local)
├── rag_db/                 → Auto-generated persistent database
├── knowledge_base.py       → Knowledge-base documents
├── 01_indexing.py          → Index documents in ChromaDB
├── 02_retrieval.py         → Semantic search and distances
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run

**1. Clone:**

```bash
git clone https://github.com/bisheytechno/namaskar-rag.git
cd namaskar-rag
```

**2. Virtual Environment:**

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

**3. Install:**

```bash
pip install -r requirements.txt
```

**4. Index Documents:**

```bash
python 01_indexing.py
```

**5. Retrieve Documents:**

```bash
python 02_retrieval.py
```

---

## Key Concepts

| Concept | What it does |
|---------|-------------|
| Embeddings | Represent text as numerical vectors |
| `PersistentClient()` | Store database data on disk |
| `get_or_create_collection()` | Get an existing collection or create one |
| `collection.add()` | Add documents to a collection |
| `collection.query()` | Retrieve similar documents |
| `query_texts` | Specify text queries for search |
| `n_results` | Set the requested number of results |
| `metadatas` | Store extra information with documents |
| `distances` | Inspect distances between query and retrieved vectors |

---

## How Retrieval Works

```text
Knowledge Base → Embeddings → ChromaDB
                                  ↓
User Query → Query Embedding → Semantic Search
                                  ↓
                         Retrieved Documents
                                  ↓
                         Distance Inspection
```

---

## RAG Pipeline

```text
Documents → Embed → Store in ChromaDB
Query     → Embed → Retrieve Documents
Results   → Build Context → Send to LLM
LLM       → Generate Answer
```

*Note: The current project implements indexing and retrieval. Context building and LLM answer generation are planned next steps.*

---

## Requirements

```text
chromadb
sentence-transformers
```

---

## Author

**Bishal KC** — Aspiring AI Engineer

GitHub: [@bisheytechno](https://github.com/bisheytechno)

---

## License

MIT License