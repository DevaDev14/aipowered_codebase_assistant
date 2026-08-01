from fastapi import FastAPI
from pydantic import BaseModel
from services.extraction import git_extraction
from services import content_embedding
from db.conn import create_collection
from db.repository import store_chunks
from llm.call_model import call_llm
from llm.prompt import build_prompt

app = FastAPI()
class IngestRequest(BaseModel):
    github_url: str
class AskRequest(BaseModel):
    question: str
    repo_name : str

@app.post("/ingest")
def ingest(request : IngestRequest):
    github_url = request.github_url
    repo_name = github_url.split('/')[-1]
    data = git_extraction.get_repo(github_url, repo_name)
    print(data)
    content_embedding.embed_chunks(data)
    collection = create_collection(repo_name)
    # print(embedded_data)
    store_chunks(collection, data)
    return {"message": "Ingested successfully"}

@app.post("/query")
def ask(request:AskRequest):
    query = request.question
    repo_name = request.repo_name
    embedding = content_embedding.query_embedding(query)
    collection = create_collection(repo_name)
    results = collection.query(
    query_embeddings=[embedding],
    n_results=5
    )
    retrieved_chunks = []
    for i in range(len(results["ids"][0])):
        retrieved_chunks.append({
            "content"   : results["documents"][0][i],
            "file_path" : results["metadatas"][0][i]["file_path"],
            "start_line": results["metadatas"][0][i]["start_line"],
            "end_line"  : results["metadatas"][0][i]["end_line"],
        })
    prompt = build_prompt(query, retrieved_chunks)
    answer = call_llm(prompt)
    return {'answer': answer }