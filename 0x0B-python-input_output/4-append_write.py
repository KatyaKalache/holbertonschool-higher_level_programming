#!/usr/bin/python3
def append_write(filename="", text=""):
    count = 0
    with open(filename, "a") as f:
        f.write(text)
    with open("file_append.txt", "r", encoding='UTF-8') as f:
        for line in f:
            for nb_characters in line:
                count += 1
            return count
