#!/usr/bin/python3
import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        importlib.reload(models.rectangle)
        importlib.reload(models.base)

    def test_wrong_num_of_args(self):
        with self.assertRaises(TypeError, msg="__init__() missing 2 required positional arguments: 'width' and 'height'"):
            Rectangle()
        with self.assertRaises(TypeError, msg="__init__() missing 1 required positional argument: 'height'"):
            Rectangle(23)
        with self.assertRaises(TypeError, msg="__init__() takes from 3 to 6 positional arguments but 8 were given"):
            Rectangle(2, 12, 23, 12, 34, 54, 23)
        
    def test_twoArgs(self):
        e = Rectangle(14, 23)
        self.assertEqual(e.width, 14)
        self.assertEqual(e.height, 23)

    def test_keyWordArgs(self):
        c = Rectangle(width=34, height=3, id=4, x=2)
        self.assertEqual(c.id, 4)
        self.assertEqual(c.width, 34)
        self.assertEqual(c.height, 3)
        self.assertEqual(c.x, 2)
        self.assertEqual(c.y, 0)

    def test_type(self):
        li = [2, 4]
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, 'dsaf', 23)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, li, 23)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle('sdf', 23, 23)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(li, 23, 23)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(2, 23, 'sdfds')
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(2, 3, li)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(2, 23, 23, 'sdfsd')
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(2, 23, 23, li)

    def test_value(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 2, 23)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(2, 0, 23)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(2, 3, -4, 23)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(2, 3, 23, -2)

    def test_area(self):
        c = Rectangle(3, 4)
        self.assertEqual(c.area(), 12)

    def test_display(self):
        a = Rectangle(2, 4, 3, 4)
        s = '\n\n\n\n   ##\n   ##\n   ##\n   ##\n'
        f = io.StringIO()
        with redirect_stdout(f):
            a.display()
        self.assertEqual(f.getvalue(), s)

    def test_update(self):
        c = Rectangle(21, 32, 44, 21, 13)
        c.update(5, 4, 3, 2, 35)
        self.assertEqual(c.id, 5)
        self.assertEqual(c.width, 4)
        self.assertEqual(c.height, 3)
        self.assertEqual(c.x, 2)
        self.assertEqual(c.y, 35)

        d = Rectangle(21, 32, 44, 21, 13)
        d.update(5, 4, 3, 2, 35, 32, 222, 343)
        self.assertEqual(d.id, 5)
        self.assertEqual(d.width, 4)
        self.assertEqual(d.height, 3)
        self.assertEqual(d.x, 2)
        self.assertEqual(d.y, 35)

        e = Rectangle(21, 32, 44, 21, 13)
        e.update(5, 4, x=35)
        self.assertEqual(e.id, 5)
        self.assertEqual(e.width, 4)
        self.assertEqual(e.x, 44)

    def test_to_dictionary(self):
        e = Rectangle(21, 32, 44, 21, 13)
        a = e.to_dictionary()
        self.assertEqual(a['width'], 21)
        self.assertEqual(a['height'], 32)
        self.assertEqual(a['x'], 44)
        self.assertEqual(a['y'], 21)
        self.assertEqual(a['id'], 13)
        s = Rectangle(21, 32)
        b = s.to_dictionary()
        self.assertEqual(b['width'], 21)
        self.assertEqual(b['height'], 32)
        self.assertEqual(b['x'], 0)
        self.assertEqual(b['y'], 0)
        self.assertEqual(b['id'], 1)

    def test_str(self):
        s = '[Rectangle] (13) 44/21 - 21/32'
        e = Rectangle(21, 32, 44, 21, 13)
        self.assertEqual(str(e), s)

    
