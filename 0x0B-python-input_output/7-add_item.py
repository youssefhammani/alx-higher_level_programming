#!/usr/bin/python3
""" Module 7-add_item
adds all arguments to a Python list
and then save them to a file
"""


import sys
import json
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_name = 'add_item.json'
item_list = []

if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
    item_list = load_from_json_file(file_name)

for e in sys.argv[1:]:
    item_list.append(e)

save_to_json_file(item_list, file_name)
