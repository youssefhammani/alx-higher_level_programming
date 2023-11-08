#!/usr/bin/python3
""" Module 7-add_item
adds all arguments to a Python list
and then save them to a file
"""


import sys
import json
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.isfile(filename):
    argument_list = load_from_json_file(filename)
else:
    argument_list = []

argument_list.extend(sys.argv[1:])

save_to_json_file(argument_list, filename)
