#!/usr/bin/python3
"""Adding 2 integers or floats module"""


def add_integer(a, b=98):
    """ Function to add 2 integers or floats

        Args:
            a: first int or float
            b: second int or float

        Raises:
            TypeError: Raise if variables are not int or float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a + b)
