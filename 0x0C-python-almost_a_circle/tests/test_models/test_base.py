#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1NoArgs(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_2TooManyArgs(self):
        b = Base()
        self.assertEqual(b.id, 1)
        self.assertRaises(TypeError, Base, 23, 43)
        b = Base()
        self.assertEqual(b.id, 2)
    
    def test_3None(self):
        a = Base(None)
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        
    def test_4Id(self):
        b = Base()
        self.assertEqual(b.id, 1)
        e = Base(14)
        self.assertEqual(e.id, 14)
        c = Base()
        self.assertEqual(c.id, 2)

    def test_5NbObjs(self):
        c = Base()
        self.assertEqual(c.id, 1)
