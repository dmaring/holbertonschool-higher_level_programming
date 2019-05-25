#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_ordered(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_unorderd(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_neg_unorderd(self):
        self.assertEqual(max_integer([-1, -3, 4, 2]), 4)

    def test_max_same_number(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_return_none(self):
        self.assertEqual(max_integer([]), None)

    def test_float(self):
        self.assertEqual(max_integer([-3.23, 23.43, 44.2]), 44.2)

    def test_string_list(self):
        with self.assertRaises(TypeError):
            max_integer('hello', 'there')

    def test_string(self):
        self.assertEqual(max_integer("hello"), 'o')

if __name__ == '__main__':
    unittest.main()
