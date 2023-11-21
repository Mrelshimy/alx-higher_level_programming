#!/usr/bin/python3
"""Creating Class that defines a square"""


class Square:
    """Square , class to define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor

        Args:
            size: square side length
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Public method to return square area"""

        return self.__size ** 2

    def my_print(self):
        """Public method for printing the square with #"""

        if self.__size == 0:
            print()

        for m in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """Getter method"""

        return self.__size

    @property
    def position(self):
        "Position Getter method"""

        return self.__position

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

    @position.setter
    def position(self, value):
        """Setter method

          Args:
              value: new square side length

          Raises:
              TypeError: check if position is 2 positive ints tuple
         """

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(j >= 0 for j in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
