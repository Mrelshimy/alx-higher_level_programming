#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 1:
    pnumber = -1 * number
else:
    pnumber = number
digit = pnumber % 10
if number < 1:
    digit = -digit
if digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
elif digit < 6:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {digit} and is greater than 5")
