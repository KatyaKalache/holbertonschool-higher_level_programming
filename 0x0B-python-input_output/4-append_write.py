#!/usr/bin/python3
"""
appends a string at the end of a text file (UTF8)
returns the number of characters added
"""


def append_write(filename="", text=""):
    count = 0
    with open(filename, "a") as f:
        f.write(text)
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            for nb_characters in line:
                count += 1
            return count
