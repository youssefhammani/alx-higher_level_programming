#!/usr/bin/python3
"""
Uses the GitHub API to list 10 commits
(from the most recent to oldest) of a repository.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')

    except requests.exceptions.HTTPError as err:
        print(f'Error: {err}')
