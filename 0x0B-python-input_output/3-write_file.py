#!/usr/bin/python3
def write_file(filename="", text=""):
    count = 0
    with open("my_first_file.txt", "w") as f:
        f.write("Holberton School is so cool!\n")

    with open("my_first_file.txt", "r") as f:
        for line in f:
            for nb_characters in line:
                count += 1
        return count
