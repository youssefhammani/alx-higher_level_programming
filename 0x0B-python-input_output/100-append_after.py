#!/usr/bin/python3
"""inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text"""
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
