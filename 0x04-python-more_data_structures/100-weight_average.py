#!/usr/bin/python3
def weight_average(my_list=[]):
    a, b, c = 0, 0, 0
    for i, j in my_list:
        a += (i * j)
        b += j
        c = a / b
    return c
