#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_int_negative(self):
        self.assertEqual(max_integer([-2, -1, -3]), -1)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 1.3, 1.4]), 1.4)

    def test_None(self):
        self.assertIsNone(max_integer([None]))

    def test_str(self):
        self.assertRaises(TypeError)
        max_integer(["str"]), "failed"

    @unittest.expectedFailure
    def test_int_str(self):
        self.assertEqual(max_integer(["Betty", 1, 2]), "failed")

if __name__ == '__main__':
    unittest.main()
