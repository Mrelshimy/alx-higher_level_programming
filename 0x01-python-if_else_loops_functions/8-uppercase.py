#!/usr/bin/python3
def isupper(str):
    for c in str:
        if ord(str[i]) >= 65 and ord(str[i]) <= 90:
            continue
        else:
            print("{:c}".format(ord(c) - 32), end="")
    print("\n")
