# 0x0B. Python - Input/Output

## Description

This project focuses on Python Input/Output operations. It covers reading and writing files, working with JSON, and handling file manipulations.

## Resources

- 7.2. Reading and Writing Files
- 8.7. Predefined Clean-up Actions
- Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))
- JSON encoder and decoder
- Learn to Program 8 : Reading / Writing Files
- Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)
- All about py-file I/O

## Learning Objectives

Upon completing this project, you should be able to explain, without using Google, the following:
- Reasons why Python programming is valuable
- How to perform file operations in Python (opening, writing, reading, and moving cursor)
- Importance and usage of the `with` statement
- Knowledge about JSON and serialization/deserialization
- Converting Python data structures to and from JSON
- Understanding and implementing serialization without exceptions

## Requirements

### Python Scripts

- Editors allowed: vi, vim, emacs
- All scripts will be interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- All files must end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Mandatory README.md file at the project root
- All Python code should follow PEP8 style (checked using pycodestyle)
- All files must be executable
- File lengths will be verified using `wc`

### Python Test Cases

- Test files should end with a new line
- All test files should be inside a folder named `tests`
- Test files should have a `.txt` extension
- Test execution: `python3 -m doctest ./tests/*`
- All modules, classes, and functions should have proper documentation
- The documentation length will be verified
- Collaboration for test cases is encouraged to cover edge cases

## Tasks

### Task 0: Read file
- Function: `def read_file(filename="")`
- Reads a text file in UTF8 and prints its content to stdout
- Usage of the `with` statement

### Task 1: Write to a file
- Function: `def write_file(filename="", text="")`
- Writes a string to a text file (UTF8) and returns the number of characters written
- Uses the `with` statement

### Task 2: Append to a file
- Function: `def append_write(filename="", text="")`
- Appends a string at the end of a text file (UTF8) and returns the number of characters added
- Uses the `with` statement

### Task 3: To JSON string
- Function: `def to_json_string(my_obj)`
- Returns the JSON representation of an object (string)

### Task 4: From JSON string to Object
- Function: `def from_json_string(my_str)`
- Returns an object represented by a JSON string

### Task 5: Save Object to a file
- Function: `def save_to_json_file(my_obj, filename)`
- Writes an object to a text file using a JSON representation

### Task 6: Create object from a JSON file
- Function: `def load_from_json_file(filename)`
- Creates an object from a JSON file

### Task 7: Load, add, save
- Script that adds all arguments to a Python list and then saves them to a file named `add_item.json`

### Task 8: Class to JSON
- Function: `def class_to_json(obj)`
- Returns a dictionary description with a simple data structure for JSON serialization of an object

### Task 9: Student to JSON
- Class `Student` with attributes: `first_name`, `last_name`, `age`
- Method `def to_json(self)` to retrieve a dictionary representation of a `Student` instance

### Task 10: Student to JSON with filter
- Extends `Student` with method `def to_json(self, attrs=None)` to retrieve a filtered dictionary representation

### Task 11: Student to disk and reload
- Extends `Student` with methods `to_json` and `reload_from_json` to replace all attributes of a `Student` instance

### Task 12: Pascal's Triangle
- Function: `def pascal_triangle(n)`
- Returns a list of lists of integers representing Pascal’s triangle of `n`

## Copyright - Plagiarism

- Solutions are to be derived without using external sources
- Strictly forbidden to publish the content of this project
- Plagiarism is a violation of the program rules

---

*© 2023 ALX. All rights reserved.*
