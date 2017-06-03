#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    count = 0
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            count += 1
            if nb_lines < 1 or nb_lines >= count:
                print(line, end="")
