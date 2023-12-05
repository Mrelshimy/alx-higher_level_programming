#!/usr/bin/python3
""" Functioon to read file and print to stdout"""


def read_file(filename=""):
    """Functioon to read file and print to stdout"""

    import sys
    with open(filename, encoding="utf-8", "r") as fp:
        for line in fp:
            print(line, file=sys.stdout)
