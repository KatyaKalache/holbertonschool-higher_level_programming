#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_int_negative(self):
        self.assertEqual(max_integer([-2, -1, -3]), -1)

if __name__ == '__main__':
    unittest.main()
