#!/usr/bin/python3
""" Add attribute method"""


def add_attribute(obj, attr, value):
    """Function to add anew attribute
    Args:
        obj : any object
        attr: new attribute to set
        value: attribute value
    Raises:
        TypeError: if not able tp add attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
