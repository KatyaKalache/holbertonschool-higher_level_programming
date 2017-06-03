#!/usr/bin/python3
"""
returns the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    if not isinstance(obj, (list, dict, str, bool, int)):
        return obj.__dict__
