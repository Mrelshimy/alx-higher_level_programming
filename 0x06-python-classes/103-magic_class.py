#!/usr/bin/python3
""" Define magic class for provided bytecode"""


import math


class MagicClass:
    """Magic Class"""

    def __init__(self, radius=0):
        """Constructor
        Args:
            radius : radius
        """

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area"""
        return self.__radis ** 2 * math.pi

    def circumference(self):
        """Return Circumference"""

        return self.__radius * 2 * math.pi
