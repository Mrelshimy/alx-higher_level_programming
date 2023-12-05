#!/usr/bin/python3
""" Function to write json representation of object to file"""
import json


def save_to_json_file(my_obj, filename):
    """Function to write json representation of object to file"""
    with open(filename, "w") as fp:
        json.dump(my_str, fp)
