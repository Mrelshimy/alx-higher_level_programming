#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    new_list = set()
    for i in my_list:
        new_list.add(i)
    for i in new_list:
        a += i
    return (a)
