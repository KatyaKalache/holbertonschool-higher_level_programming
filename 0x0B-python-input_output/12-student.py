#!/usr/bin/python3
import json
"""
For attrs in list of strings, only attributes name from list must be retrieved.
"""


class Student:
    def __init__(self, first_name, last_name, age):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            for i in attrs:
                if hasattr(self, i):
                    return json.dumps(i)
             #   else:
              #      return json.loads(json.dumps(self.__dict__, i))
        if attrs is None:
            return json.loads(json.dumps(self.__dict__, attrs))
