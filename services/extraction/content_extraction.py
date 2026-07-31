from pathlib import Path
from services.extraction.chunker import code_chunker
from services.content_embedding import embed_chunks

def get_path(path):
    dir = Path(path)
    documents = [] 
    all_chunks = []
    for module in dir.rglob('*.py'):
        content = module.read_text(
            encoding="utf-8",
            errors='ignore'
        )
        documents.append({'path': str(module),'content': content})
    for doc in documents:
        chunks = code_chunker(doc)
        all_chunks.extend(chunks)

    return all_chunks

if __name__ == '__main__':
    path = r'D:\genai\codebase_assistant\git_repos\httpx'
    chunks = get_path(path)
    embedded_data = embed_chunks(chunks)
    print(embedded_data[0]["name"])
    print(len(embedded_data[0]["embedding"])) 
    print(embedded_data[0]["embedding"][:3])

    # for chunk in chunks[:3]:
    #     print("─" * 50)
    #     print(f"Name      : {chunk['name']}")
    #     print(f"Type      : {chunk['type']}")
    #     print(f"File      : {chunk['file_path']}")
    #     print(f"Lines     : {chunk['start_line']} → {chunk['end_line']}")
    #     print(f"Content   :\n{chunk['content']}")