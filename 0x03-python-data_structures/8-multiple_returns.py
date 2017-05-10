#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = sentence[0]
    if sentence is None:
        first_char = "None"
    return(len(sentence), first_char)
