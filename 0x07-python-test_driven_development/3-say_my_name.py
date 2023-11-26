#!/usr/bin/python3
"""module for printing full name"""


def say_my_name(first_name, last_name=""):
    """ Function to print full name

        Args:
            first_name: first name
            last_name: last name

        Raises:
            TypeError: first_nme or last_name are is not string

        Returns:
            My Name is first_name last_name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My Name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
