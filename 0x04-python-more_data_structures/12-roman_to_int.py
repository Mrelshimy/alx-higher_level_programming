#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    rom_alpha = {'I': 1, 'V': 5,
                 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    list = []
    for i in roman_string:
        list.append(rom_alpha[i])
    for i in range(0, len(list)):
        if i < len(list) - 1 and list[i] < list[i + 1]:
            total -= list[i]
        else:
            total += list[i]
    return total
