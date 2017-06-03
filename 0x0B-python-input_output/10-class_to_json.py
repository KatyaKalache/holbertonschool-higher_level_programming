#!/usr/bin/python3
"""
returns the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    if obj is not None:
        return obj.__dict__
