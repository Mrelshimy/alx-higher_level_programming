#!/usr/bin/python3
"""Check object is exactly an instance of class"""


def inherits_from(obj, a_class):
    """compare object and class instance"""

    return type(obj) != a_class and isinstance(obj, a_class)
