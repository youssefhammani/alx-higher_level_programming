#!/usr/bin/python3
""" Module 7-add_item
adds all arguments to a Python list
and then save them to a file
"""


import json
import sys
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv[1:]

filename = "add_item.json"

if not os.path.exists(filename):
    save_to_json_file([], filename)

data = load_from_json_file(filename)
data += args

save_to_json_file(data, filename)
