#!/usr/bin/python3
""" Module 7-add_item
adds all arguments to a Python list
and then save them to a file
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

existing_list = load_from_json_file("add_item.json") if load_from_json_file("add_item.json") else []

existing_list += sys.argv[1:]

save_to_json_file(existing_list, "add_item.json")
