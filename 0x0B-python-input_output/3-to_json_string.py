#!/usr/bin/python3
""" Function to return json representation of object"""
import json


def to_json_string(my_obj):
    """Function to return json representation of object"""
    return json.dumb(my_obj)
