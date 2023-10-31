#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range (0, 10):
        if num1 == num2 or num2 < num1:
            continue
        elif num1 != 8 or num2 != 9:
            print("{}{}, ".format(num1, num2).format(num1, num2), end="")
        else:
            print(89)
