#!/usr/bin/python3
def print_last_digit(number):
    if number < 1:
        number = -1 * number
    digit = pnumber % 10
    if number < 1:
        digit = -digit
    print(digit, end="")
    return digit
