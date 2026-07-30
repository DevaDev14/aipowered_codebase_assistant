from pathlib import Path

def get_path(path):
    dir = Path(path)
    documents = [] 
    for module in dir.rglob('*.py'):
        content = module.read_text(
            encoding="utf-8",
            errors='ignore'
        )
        documents.append({'path': str(module),'content': content})
    print(documents[0])

if __name__ == '__main__':
    path = r'D:\genai\codebase_assistant\git_repos\httpx'
    get_path(path)