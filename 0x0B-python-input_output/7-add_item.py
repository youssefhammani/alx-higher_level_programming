#!/usr/bin/python3
""" Module 7-add_item
adds all arguments to a Python list
and then save them to a file
"""


import sys
import os

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

args = sys.argv[1:]

filename = "add_item.json"

if not os.path.exists(filename):
    save_to_json_file([], filename)

data = load_from_json_file(filename)
data.extend(args)

save_to_json_file(data, filename)
