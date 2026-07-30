from fastapi import FastAPI
from pydantic import BaseModel
from services.extraction import git_extraction

app = FastAPI()

class IngestRequest(BaseModel):
    github_url: str
class AskRequest(BaseModel):
    question: str

@app.post("/ingest")
def ingest(request : IngestRequest):
    github_url = request.github_url
    repo_name = github_url.split('/')[-1]
    git_extraction.get_repo(github_url, repo_name)
    return {"message": "Ingested successfully"}