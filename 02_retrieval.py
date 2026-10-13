import chromadb
from chromadb.utils import embedding_functions


embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path="./rag_db")

collection = client.get_or_create_collection(
    name = "rag_knowledge",
    embedding_function= embedding_fn
)

print("Total documents: ", collection.count())


# query = "What is RAG?"

# results = collection.query(
#     query_texts = [query],
#     n_results=3
# )

# for document in results['documents'][0]:
#     print(document)
#     print("---")

query = "What is RAG?"

results = collection.query(
    query_texts= [query],
    n_results=3,
    include = ["documents","distances", "metadatas"]
)

for i, document in enumerate(results["documents"][0]):
    distance = results["distances"][0][i]

    print(f"Document: {document}")
    print(f"Distance : {distance:.4f}")
    print("----")