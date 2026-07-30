from git import Repo
from path_extraction import get_path

def get_repo(repo_url, repo_name):
    directory = fr"{repo_url}{repo_name}"
    print(fr"{repo_url}/{repo_name}")
    Repo.clone_from(
        repo_url,
        directory
    )
    get_path(directory)

if __name__ == '__main__':
    repo_url = r'https://github.com/encode/httpx'
    repo_name = repo_url.split('/')[-1]
    directory = get_repo(repo_url, repo_name)