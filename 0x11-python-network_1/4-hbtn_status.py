#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    content_type = type(response.text)

    print("Body response:")
    print("\t- type: {}".format(content_type))
    print("\t- content: {}".format(response.text))
