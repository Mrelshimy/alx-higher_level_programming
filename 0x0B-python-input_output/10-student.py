#!/usr/bin/python3
"""Student Class Module"""


class Student:
    """Class to define student data"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return json representation for student data fir keys in attrs"""
        for attr in attrs:
            if type(attr) not str:
                return self.__dict__
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
