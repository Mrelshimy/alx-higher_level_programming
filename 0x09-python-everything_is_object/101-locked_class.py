#!/usr/bin/python3
"""Locked Class Module"""


class LockedClass:
    """
    Class with locked attribute to prevent creation
    of any attribute with name other than "first_name"
    """

    __slots__ = ["first_name"]
