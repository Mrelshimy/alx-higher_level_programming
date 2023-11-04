#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        char = "None"
    else:
        char = sentence[0]
    result = (length, char)
    return result
