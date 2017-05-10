#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = sentence[0]
    length = len(sentence)
    if length == 0:
        first_char = None
    return(length, first_char)
