#!/usr/bin/python3
def isupper(str):
    while (str[i]):
        if ord(str[i]) >= 65 and ord(str[i]) <= 90:
            continue
        else:
            a = ord(str[i])
	    a -= 32
	    str[i] = chr(a)
    print(str[i], end="")
