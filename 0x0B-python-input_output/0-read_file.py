#!/usr/bin/python3
""" Functioon to read file and print to stdout"""


def read_file(filename=""):
    """Functioon to read file and print to stdout"""
    with open(filename, encoding='utf-8') as fp:
        print(fp.read(), end="")
