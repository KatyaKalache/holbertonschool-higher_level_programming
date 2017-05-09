#!/usr/bin/python3
i = 122
while i > 96:
    copy = i
    if (i % 2) != 0:
        copy = i - 32
    print('{:}'.format(chr(copy)), end='')
    i = i - 1
