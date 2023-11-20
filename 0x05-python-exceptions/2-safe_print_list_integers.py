#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            i += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print()
    return i
