#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def max_integer(self):
        values = [1, 2, 3]
        result = max_integer(self)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
