#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    biggest = None
    for i in a_dictionary:
        if a_dictionary[i] > max:
            max = a_dictionary[i]
            biggest = i
    return biggest
