#!/usr/bin/python3
def number_of_lines(filename=""):
    count = 0
    with open("my_file_0.txt") as f:
        for line in f:
            count += 1
    return count        
