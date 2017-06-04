#!/usr/bin/python3
"""
For attrs in list of strings,
only attributes name from list must be retrieved.
"""


class Student:
    def __init__(self, first_name, last_name, age):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

    def to_json(self, attrs=None):
        match = {}
        if attrs is not None:
            for i in range(len(attrs)):
                if hasattr(self, attrs[i]):
                    match[attrs[i]] = getattr(self, attrs[i])
            return match

        if attrs is None:
            return self.__dict__

    def reload_from_json(self, json):
        if hasattr(json, "first_name"):
            setattr(self.first_name, first_name)
            if hasattr(json, "last_name"):
                setattr(self.last_name, last_name)
                if hasattr(json, "age"):
                    setattr(self.age, age)
