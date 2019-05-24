#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular(self):
        reg = [3, 8, 3, 2]
        self.assertEqual(max_integer(reg), 8)

    def test_not_all_nums(self):
        reg = [[3, 4, 5], 'dfs', 3, 2]
        self.assertEqual(max_integer(reg), 8)

    def test_regular(self):
        reg = [3, 8, 3, 2]
        self.assertEqual(max_integer(reg), 8)

    def test_regular(self):
        reg = [3, 8, 3, 2]
        self.assertEqual(max_integer(reg), 8)

    def test_regular(self):
        reg = [3, 8, 3, 2]
        self.assertEqual(max_integer(reg), 8)

    def test_regular(self):
        reg = [3, 8, 3, 2]
        self.assertEqual(max_integer(reg), 8)
