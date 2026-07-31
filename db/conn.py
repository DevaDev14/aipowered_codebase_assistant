import chromadb

def create_collection(collection_name="codebase"):
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name=collection_name)
    return collection