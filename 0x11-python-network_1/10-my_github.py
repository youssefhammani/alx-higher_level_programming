#!/usr/bin/python3
"""
Uses Basic Authentication with a personal access token
to display the GitHub user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))

    try:
        json_response = response.json()
        print(json_response.get('id'))
    except ValueError:
        print(None)
