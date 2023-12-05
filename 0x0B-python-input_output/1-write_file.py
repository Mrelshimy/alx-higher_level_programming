#!/usr/bin/python3
""" Functioon to write string to file"""


def write_file(filename="", text=""):
    """Functioon to write string to file"""
    with open(filename, encoding='utf-8',  "w") as fp:
        fp.write(filename, text)
