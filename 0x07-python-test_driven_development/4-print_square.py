#!/usr/bin/python3
"""module for printing square of #"""


def print_square(size):
    """ Function to print square of #

        Args:
            size: square side length

        Raises:
            TypeError: Raise if size is float
            ValueError: Raise if size is < 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
