#!/usr/bin/python3
"""Creating Class that defines a square"""


class Square:
    """Square , class to define a square"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: square side length
        """
        self.__size = size

    def area(self):
        """Public method to return square area"""

        return self.__size ** 2

    @property
    def size(self):
        """Getter method"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter method

        Args:
            value: new square side length

        Raises:
            TypeError: check if size is integer
            ValueError: check if size is > 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
