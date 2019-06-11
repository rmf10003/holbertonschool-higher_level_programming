#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_1NoArgs(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_2TooManyArgs(self):
        self.assertRaises(TypeError, Base, 23, 43)
    
    def test_3None(self):
        a = Base(None)
        self.assertEqual(a.id, 2)
        
    def test_4Id(self):
        e = Base(14)
        self.assertEqual(e.id, 14)

    def test_5NbObjs(self):
        c = Base()
        self.assertEqual(c.id, 3)
