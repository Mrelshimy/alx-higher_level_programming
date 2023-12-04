#!/usr/bin/python3
""" Module to returns the list of attributes and methods of object"""


def lookup(obj):
    """Function to return object __dict___"""

    return dir(obj)
