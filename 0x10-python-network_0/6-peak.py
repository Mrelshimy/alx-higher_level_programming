#!/usr/bin/python3
"""Find a peak module"""


def find_peak(list_of_integers):
    """Function to find a peak in unsorted list"""
    if not list_of_integers:
        return None
    z = 0
    for item in list_of_integers:
        if item >= z:
            z = item
    return z
