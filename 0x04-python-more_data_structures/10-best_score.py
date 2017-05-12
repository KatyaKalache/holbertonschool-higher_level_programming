#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    max_val = max(list(my_dict.values()))
    for key, value in my_dict.items():
        if value == max_val:
            return key
