from git import Repo

def get_repo(repo_url, repo_name):
    Repo.clone_from(
        repo_url,
        fr"D:\genai\codebase_assistant\git_repos\{repo_name}"
    )

if __name__ == '__main__':
    repo_url = r'https://github.com/encode/httpx'
    repo_name = repo_url.split('/')[-1]
    directory = get_repo(repo_url, repo_name)
