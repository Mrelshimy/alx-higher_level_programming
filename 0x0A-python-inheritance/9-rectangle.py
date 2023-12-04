#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area calculation method"""
        return self.__height * self.__width

    def __str__(self):
        """printing data method"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
