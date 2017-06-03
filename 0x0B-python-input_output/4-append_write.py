#!/usr/bin/python3
"""
appends a string at the end of a text file (UTF8)
returns the number of characters added
"""


def append_write(filename="", text=""):
    with open(filename, "a") as f:
        count = f.write(text)
        return count
