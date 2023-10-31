#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{:c}".format(ord(c)
              if ord(c) >= 65 and ord(c) <= 90 else ord(c) - 32))
    print("")
