#!/usr/bin/python3
def uppercase(s):
    output = ""
    for char in s:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:
            uppercase_ascii = ascii_value - 32
            output += "{}".format(chr(uppercase_ascii))
        else:
            output += "{}".format(char)
    print("{}".format(output))
