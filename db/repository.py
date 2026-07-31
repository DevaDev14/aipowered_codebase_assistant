def store_chunks(collection, chunks):
    ids        = []
    embeddings = []
    documents  = []
    metadatas  = []
    for chunk in chunks:
        ids.append(chunk["name"] + "_" + chunk["file_path"])
        embeddings.append(chunk["embedding"])
        documents.append(chunk["content"])
        metadatas.append({
            "file_path" : chunk["file_path"],
            "name"      : chunk["name"],
            "type"      : chunk["type"],
            "start_line": chunk["start_line"],
            "end_line"  : chunk["end_line"],
        })
    collection.add(
        ids        = ids,
        embeddings = embeddings,
        documents  = documents,
        metadatas  = metadatas,
    )

def search_data(vector):
    pass
