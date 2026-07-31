from git import Repo
from services.extraction.content_extraction import get_path


def get_repo(repo_url, repo_name):
    directory = fr"D:\genai\codebase_assistant\git_repos\{repo_name}"
    Repo.clone_from(
        repo_url,
        directory
    )
    return get_path(directory)

if __name__ == '__main__':
    repo_url = r'https://github.com/psf/requests'
    repo_name = repo_url.split('/')[-1]
    directory = get_repo(repo_url, repo_name)