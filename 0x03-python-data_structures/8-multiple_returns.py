#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return
    first_char = sentence[0]
    if len(sentence) == 0:
        first_char = "None"
    return(len(sentence), first_char)
