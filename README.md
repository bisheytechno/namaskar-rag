# Namaskar RAG 🧠

Learning Retrieval-Augmented Generation (RAG) using Python and ChromaDB — a foundation for AI engineering.

---

## What This Covers

- Document indexing — store knowledge-base documents
- Text embeddings — convert text into numerical vectors
- Persistent storage — save data using ChromaDB
- Semantic search — retrieve relevant documents
- Distance inspection — analyze retrieval results
- Context building — combine retrieved documents into a single context string

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
├── myvenv/                    → Virtual environment (local)
├── rag_db/                    → Auto-generated persistent database
├── knowledge_base.py           → Knowledge-base documents
├── 01_indexing.py              → Index documents in ChromaDB
├── 02_retrieval.py             → Semantic search and distances
├── 03_context_building.py      → Build context from retrieved documents
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

**2. Create a Virtual Environment:**

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

**3. Install Dependencies:**

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

**6. Build Context:**

```bash
python 03_context_building.py
```

---

## Key Concepts

| Concept | What it does |
|---------|-------------|
| `SentenceTransformerEmbeddingFunction()` | Configures the text embedding function |
| `PersistentClient()` | Stores database data on disk |
| `get_or_create_collection()` | Gets an existing collection or creates one |
| `collection.add()` | Adds documents to a collection |
| `collection.query()` | Retrieves similar documents |
| `query_texts` | Specifies text queries for search |
| `n_results` | Sets the requested number of results |
| `metadatas` | Stores extra information with documents |
| `distances` | Provides distances for retrieved results |
| `enumerate()` | Iterates over items with their indices |
| `"\n\n".join(documents)` | Combines document strings with blank lines |

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

## Context Building

```text
User Query
    ↓
ChromaDB Retrieval
    ↓
Retrieved Documents
    ↓
Combine Documents Using join()
    ↓
Single Context String
```

The retrieved documents are combined into one text string that can later be provided to a language model as context.

---

## RAG Pipeline

```text
Documents → Embed → Store in ChromaDB
Query     → Embed → Retrieve Documents
Results   → Build Context → Send to LLM
LLM       → Generate Answer
```

**Current progress:** Document indexing, semantic retrieval, distance inspection, and context building have been implemented as separate scripts. LLM integration and final answer generation are the next steps.

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