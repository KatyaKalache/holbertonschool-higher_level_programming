#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        Rectangle.integer_validator(self, "size", size)

    def area(self):
        result = self.__size * self.__size
        return result

    def __str__(self):
        return("[{:s}] {}/{}".format(type(self).__name__, self.__size, self.__size))
