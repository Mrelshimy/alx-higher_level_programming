#!/usr/bin/python3
def isupper(str):
    for c in str:
        if ord(c) >= 65 and ord(c) <= 90:
            print("{}".format(c), end="")
        else:
            print("{:c}".format(ord(c) - 32), end="")
