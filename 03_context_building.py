import chromadb
from chromadb.utils import embedding_functions

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path="./rag_db")
collection = client.get_or_create_collection(
    name="rag_knowledge",
    embedding_function=embedding_fn
)

query = "What is RAG?"

results = collection.query(
    query_texts=[query],
    n_results=3,
    include=["documents", "distances", "metadatas"]
)

documents = results["documents"][0]
context = "\n\n".join(documents)

print("USER QUESTION:")
print(query)

print("\nRETRIEVED CONTEXT:")
print(context)
