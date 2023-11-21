#!/usr/bin/python3
"""Creating Class that defines a square"""


class Square:
    """Square , class to define a square"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: square side length

        Raises:
            TypeError: check if size is integer
            ValueError: check if size is > 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public method to return square area"""

        return self.__size ** 2
