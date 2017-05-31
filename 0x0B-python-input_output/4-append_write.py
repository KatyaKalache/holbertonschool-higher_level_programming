#!/usr/bin/python3
def append_write(filename="", text=""):
    count = 0
    with open("file_append.txt", "a") as f:
        f.write("Holberton School is so cool!\n")
    with open("file_append.txt", "r") as f:
        for line in f:
            for nb_characters in line:
                count += 1
            return count
