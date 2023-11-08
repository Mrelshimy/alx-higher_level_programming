#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for item in a_dictionary:
        if a_dictionary[item] == value:
            del item
    return (a_dictionary)
