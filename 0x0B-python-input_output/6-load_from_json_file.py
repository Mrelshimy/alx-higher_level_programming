#!/usr/bin/python3
""" Function to create object from json file"""
import json


def load_from_json_file(filename):
    """Function to create object from json file"""
    with open(filename, encoding='utf-8') as fp:
        return json.load(fp)
