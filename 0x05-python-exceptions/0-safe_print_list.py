#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for element in range (x):
            print("{}".format(my_list[element]), end="")
        print()
        return x
    except:
        for element in my_list:
            i += 1
        print()
        return i
