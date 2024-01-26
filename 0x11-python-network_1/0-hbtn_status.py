#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')

print("Body response:")
print("    - type:", type(body))
print("    - content:", body)
print("    - utf8 content:", utf8_content)
