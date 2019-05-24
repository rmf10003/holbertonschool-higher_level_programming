#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test"""
    def test_regular(self):
        """test"""
        self.assertEqual(max_integer([23, 2, 3, 4]), 23)

    def test_somefloats(self):
        """test"""
        self.assertEqual(max_integer([23, 4, 3.2, 444.3]), 444.3)

    def test_strings(self):
        """test"""
        self.assertEqual(max_integer(['d', 's', 'r', 'd']), 's')

    def test_empty(self):
        """test"""
        self.assertEqual(max_integer(), None)

    def test_none(self):
        """test"""
        error = "object of type 'NoneType' has no len()"
        with self.assertRaises(TypeError, msg=error):
            max_integer(None)

    def test_mixing_types(self):
        """tests for """
        error = "unorderable types: str() > int()"
        with self.assertRaises(TypeError, msg=error):
            max_integer([23, 4, 3.2, 'd'])

    def test_mult_args(self):
        """tests for """
        error = "max_integer() takes from \
        0 to 1 positional arguments but 2 were given"
        with self.assertRaises(TypeError, msg=error):
            max_integer([23, 4, 3.2, 2], [2, 3])
