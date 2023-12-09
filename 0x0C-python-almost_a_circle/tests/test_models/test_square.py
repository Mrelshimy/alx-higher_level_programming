#!/usr/bin/python3
"""Testing base class module"""
import unittest
import os
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Testing base class"""

    def setUp(self):
        '''instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def test_inheritance(self):
        s = Square(1, 1)
        self.assertTrue(isinstance(s, Base))

    def test_args(self):
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, 4, 5)

    def test_getters(self):
        r = Square(1, 2, 3, 4)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 4)

    def test_setters(self):
        r = Square(1, 2, 3, 4)
        r.size = 11
        r.x = 12
        r.y = 13
        r.id = 14
        self.assertEqual(r.size, 11)
        self.assertEqual(r.x, 12)
        self.assertEqual(r.y, 13)
        self.assertEqual(r.id, 14)

    def test_size_value(self):
        with self.assertRaises(ValueError) as e:
            r1 = Square(-1, 1)
        with self.assertRaises(TypeError) as e:
            r1 = Square("hi", 1)

    def test_x_value(self):
        with self.assertRaises(ValueError) as e:
            r1 = Square(1, -1)
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, "hi")

    def test_y_value(self):
        with self.assertRaises(ValueError) as e:
            r1 = Square(1, 1, -1)
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 1, "hi")

    def test_area(self):
        r = Square(2)
        self.assertEqual(r.area(), 4)

    def test_display(self):
        r = Square(2, 2, 2)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            r.display()
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")

    def test_print(self):
        r = Square(2, 1, 1, 100)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            print(r)
        self.assertEqual(output.getvalue(), "[Square] (100) 1/1 - 2\n")

    def test_update(self):
        r = Square(1, 1, 1, 100)
        r1 = Square(5, 5, 5, 101)
        r1_dict = r1.to_dictionary()
        r.update(**r1_dict)
        self.assertFalse(r == r1)
        self.assertFalse(r is r1)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            print(r)
        self.assertEqual(output.getvalue(), "[Square] (101) 5/5 - 5\n")
        r3 = Square(5, 2)
        r3.update(10)
        self.assertEqual(r3.id, 10)
        r3.update(10, 5)
        self.assertEqual(r3.size, 5)
        r3.update(10, 5, 17)
        self.assertEqual(r3.x, 17)
        r3.update(10, 5, 17, 20)
        self.assertEqual(r3.y, 20)

    def test_to_dictionary(self):
        r1 = Square(1, 1, 1, 100)
        r2 = Square(2, 2, 2)
        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()
        self.assertEqual(r1_dict, {'x': 1, 'y': 1, 'id': 100, 'size': 1})
        self.assertEqual(r2_dict, {'x': 2, 'y': 2, 'id': 1, 'size': 2})
