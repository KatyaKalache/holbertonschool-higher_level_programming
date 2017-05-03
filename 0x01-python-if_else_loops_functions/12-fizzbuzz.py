#!/usr/bin/python3
def fizzbuzz():
    number = 1
    while number <= 100:
        if number % 3 == 0 and number % 5 !=0:
            print('Fizz ', end='')
        elif number % 5 == 0 and number % 3 != 0:
            print('Buzz ', end='')
        elif number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz ', end='')
        else:
            print('{:d} '.format(number), end='')
        number = number + 1
