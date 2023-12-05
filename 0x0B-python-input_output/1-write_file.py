#!/usr/bin/python3
""" Functioon to write string to file"""


def write_file(filename="", text=""):
    """Functioon to write string to file"""
    with open(filename, "w", encoding='utf-8') as fp:
        return fp.write(text)
