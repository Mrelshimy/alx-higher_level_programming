#!/usr/bin/python3
"""Class Rectangle module"""


class Rectangle:
    """
    Class to define Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Constructor

        Args:
            width: rectangle width
            height: rectangle height

        Raises:
            TypeError: height or width not int
            ValueError: height or width < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """heigth setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method to return rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """Method to return rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.width + self.height))
