#!/usr/bin/python3
""" Function to return json representation of object"""
import json


def from_json_string(my_str):
    """Function to return json representation of object"""
    return json.loads(my_str)
