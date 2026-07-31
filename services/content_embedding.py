from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer("BAAI/bge-m3")

def embed_chunks(chunks):
    texts = [chunk["content"] for chunk in chunks]
    embeddings = embed_model.encode(texts, batch_size=8, show_progress_bar=True)
    for i, chunk in enumerate(chunks):
        chunk["embedding"] = embeddings[i].tolist()
    return chunks

def query_embedding(query):
    embedding = embed_model.encode(query, batch_size=8, show_progress_bar=True).tolist()
    return embedding