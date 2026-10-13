import chromadb
from chromadb.utils import embedding_functions
from knowledge_base import DOCUMENTS

# Setup
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path="./rag_db")

collection = client.get_or_create_collection(
    name="rag_knowledge",
    embedding_function=embedding_fn
)

# Already stored xa bhane skip gara!
if collection.count() == 0:
    collection.add(
        documents=DOCUMENTS,
        metadatas=[{"doc_id": i} for i in range(len(DOCUMENTS))],
        ids=[f"doc{i}" for i in range(len(DOCUMENTS))]
    )
    print(f"✅ {len(DOCUMENTS)} documents indexed!")
else:
    print(f"✅ Already indexed: {collection.count()} docs")