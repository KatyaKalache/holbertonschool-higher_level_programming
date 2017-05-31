#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

    def area(self):
        result = self.__width * self.__height
        return result

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

