from fastapi import FastAPI
from pydantic import BaseModel
from services.extraction import git_extraction
from services import content_embedding
from db.conn import create_collection
from db.repository import store_chunks

app = FastAPI()

class IngestRequest(BaseModel):
    github_url: str
class AskRequest(BaseModel):
    question: str

@app.post("/ingest")
def ingest(request : IngestRequest):
    github_url = request.github_url
    repo_name = github_url.split('/')[-1]
    data = git_extraction.get_repo(github_url, repo_name)
    embedded_data = content_embedding.embed_chunks(data)
    collection = create_collection(repo_name)
    store_chunks(collection, data)
    return {"message": "Ingested successfully"}