#!/usr/bin/python3
def print_last_digit(number):
        ld = number % 10
    if number < 0:
        number = number * -1
        print('{:d}'.format(ld), end='')
    else:
        print('{:d}'.format(ld), end='')
    return ld
