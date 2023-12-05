#!/usr/bin/python3
"""Student Class Module"""


class Student:
    """Class to define student data"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return json representation for student data"""
        return self.__dict__
