#!/usr/bin/python3
""" Functioon to append string to file"""


def append_write(filename="", text=""):
    """Functioon to append string to file"""
    with open(filename, "a", encoding='utf-8') as fp:
        return fp.write(text)
