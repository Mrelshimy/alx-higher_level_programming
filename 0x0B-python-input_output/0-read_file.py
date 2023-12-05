#!/usr/bin/python3
""" Functioon to read file and print to stdout"""


def read_file(filename=""):
    """Functioon to read file and print to stdout"""

    import sys
    with open(filename, encoding="UTF8", "r") as fp:
            print(fp.read(), file=sys.stdout)
