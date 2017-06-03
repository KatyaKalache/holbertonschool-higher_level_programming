#!/usr/bin/python3
"""
writes a string to a text file (UTF8)
returns the number of characters written
"""


def write_file(filename="", text=""):
    count = 0
    with open(filename, "w",  encoding='UTF-8') as f:
        f.write(text)

    with open(filename, "r") as f:
        for line in f:
            for nb_characters in line:
                count += 1
        return count
