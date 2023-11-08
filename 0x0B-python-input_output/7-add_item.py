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

my_file = 'add_item.json'

my_list = load_from_json_file(my_file) if load_from_json_file(my_file) else []

my_list += sys.argv[1:]

save_to_json_file(my_list, my_file)
