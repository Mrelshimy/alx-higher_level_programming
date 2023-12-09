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
        r = Rectangle(1, 1)
        self.assertTrue(isinstance(r, Base))

    def test_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_getters(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_setters(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 11
        r.height = 12
        r.x = 13
        r.y = 14
        r.id = 15
        self.assertEqual(r.width, 11)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 13)
        self.assertEqual(r.y, 14)
        self.assertEqual(r.id, 15)

    def test_width_value(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(-1, 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle("hi", 1)

    def test_height_value(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, -1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, "hi")

    def test_x_value(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 1, -1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, "hi")

    def test_y_value(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 1, 1, -1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, 1, "hi")

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        r = Rectangle(2, 2, 2, 2)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            r.display()
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n")

    def test_print(self):
        r = Rectangle(2, 2, 1, 1, 100)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            print(r)
        self.assertEqual(output.getvalue(), "[Rectangle] (100) 1/1 - 2/2\n")

    def test_update(self):
        r = Rectangle(1, 1, 1, 1, 100)
        r1 = Rectangle(5, 5, 5, 5, 101)
        r1_dict = r1.to_dictionary()
        r.update(**r1_dict)
        self.assertFalse(r == r1)
        self.assertFalse(r is r1)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            print(r)
        self.assertEqual(output.getvalue(), "[Rectangle] (101) 5/5 - 5/5\n")

        r3 = Rectangle(5, 2)
        r3.update(10)
        self.assertEqual(r3.id, 10)
        r3.update(10, 5)
        self.assertEqual(r3.width, 5)
        r3.update(10, 5, 17)
        self.assertEqual(r3.height, 17)
        r3.update(10, 5, 17, 20)
        self.assertEqual(r3.x, 20)
        r3.update(10, 5, 17, 20, 25)
        self.assertEqual(r3.y, 25)

    def test_to_dictionary(self):
        r1 = Rectangle(1, 1, 1, 1, 100)
        r2 = Rectangle(2, 2, 2, 2)
        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()
        self.assertEqual(r1_dict,
                         {'x': 1, 'y': 1, 'id': 100, 'height': 1, 'width': 1})
        self.assertEqual(r2_dict,
                         {'x': 2, 'y': 2, 'id': 1, 'height': 2, 'width': 2})
