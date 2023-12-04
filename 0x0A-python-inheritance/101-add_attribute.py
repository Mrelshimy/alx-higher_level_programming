#!/usr/bin/python3
""" Add attribute method"""


def add_attribute(obj, attr, value):
    """Function to add anew attribute"""

    if not hasattr(obj, "__dict__"):
        raise TyprError("can't add new attribute")
    return setattr(obj, attr, value)
