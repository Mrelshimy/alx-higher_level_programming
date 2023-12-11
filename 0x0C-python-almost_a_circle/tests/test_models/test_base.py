#!/usr/bin/python3
"""Testing base class module"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Testing base class"""

    def setUp(self):
        '''instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def test_id(self):
        """Test id various values"""
        new1 = Base()
        self.assertEqual(new1.id, 1)
        new2 = Base(10)
        self.assertEqual(new2.id, 10)
        new3 = Base()
        self.assertEqual(new3.id, 2)
        new4 = Base("new4")
        self.assertEqual(new4.id, "new4")
        new5 = Base(-1)
        self.assertEqual(new5.id, -1)
        new6 = Base(id=30)
        self.assertEqual(new6.id, 30)

    def test_to_json_string(self):
        """Test to json string function"""
        list1 = []
        list2 = None
        list3 = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8},
                 {'x': 2, 'width': 10, 'id': 1, 'y': 8}]
        list4 = "hi"
        list5 = [{}]
        list6 = [{}, {}]
        r1 = Rectangle(1, 1, 1, 1)
        r1_dict = r1.to_dictionary()
        r1_json = r1.to_json_string(r1_dict)
        r1_dict = str(r1_dict)
        r1_dict = r1_dict.replace("'", '"')
        self.assertEqual(r1_dict, r1_json)
        s1 = Square(1, 1, 1, 1)
        s1_dict = s1.to_dictionary()
        s1_json = s1.to_json_string(s1_dict)
        s1_dict = str(s1_dict)
        s1_dict = s1_dict.replace("'", '"')
        self.assertEqual(s1_dict, s1_json)
        with self.assertRaises(TypeError):
            Base.to_json_string()
        self.assertEqual(Base.to_json_string(list1), "[]")
        self.assertEqual(Base.to_json_string(list2), "[]")
        self.assertEqual(Base.to_json_string(list3),
                         '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, {"x": 2, "width": 10, "id": 1, "y": 8}]')
        self.assertEqual(Base.to_json_string(list4), '"hi"')
        self.assertEqual(Base.to_json_string(list5), '[{}]')
        self.assertEqual(Base.to_json_string(list6), '[{}, {}]')

    def test_from_json_string(self):
        """Test from json string function"""
        string1 = ""
        string2 = None
        string3 = '[{}]'
        string4 = '[{}, {}]'
        string5 = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, \
                    {"x": 2, "width": 10, "id": 1, "y": 8}]'
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        self.assertEqual(Base.from_json_string(string3), [{}])
        self.assertEqual(Base.from_json_string(string4), [{}, {}])
        self.assertEqual(Base.from_json_string(string1), [])
        self.assertEqual(Base.from_json_string(string2), [])
        self.assertEqual(Base.from_json_string(string5),
                         [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8},
                          {"x": 2, "width": 10, "id": 1, "y": 8}])

    def test_create(self):
        """Test create function"""
        r1 = Rectangle(1, 2, 0, 0)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        s1 = Square(1, 0, 0)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertFalse(s1 is s2)
        self.assertTrue(isinstance(s2, Square))

    def test_save_to_file(self):
        r1 = Rectangle(1, 1, 1, 1)
        r2 = Square(1, 1, 1)
        obj_list = [r1, r2]
        Base.save_to_file(obj_list)
        with open("Base.json", encoding='utf-8') as fp:
            data = fp.read()
        expected_op = '[{"x": 1, "y": 1, "id": 1, "height": 1, "width": 1}, {"id": 2, "x": 1, "size": 1, "y": 1}]'
        self.assertEqual(data, expected_op)
        os.remove("Base.json")

    def test_load_from_file(self):
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        obj_list = [r1, r2]
        Rectangle.save_to_file(obj_list)
        new_list = Rectangle.load_from_file()
        self.assertEqual(len(new_list), 2)
        self.assertTrue(obj_list, new_list)
        self.assertNotEqual(id(obj_list), id(new_list))
        self.assertEqual(str(obj_list[0]), str(new_list[0]))
        self.assertEqual(str(obj_list[1]), str(new_list[1]))
        os.remove("Rectangle.json")

        s1 = Square(1)
        s2 = Square(2)
        sobj_list = [s1, s2]
        Square.save_to_file(sobj_list)
        snew_list = Square.load_from_file()
        self.assertEqual(len(snew_list), 2)
        self.assertTrue(sobj_list, snew_list)
        self.assertNotEqual(id(sobj_list), id(snew_list))
        self.assertEqual(str(sobj_list[0]), str(snew_list[0]))
        self.assertEqual(str(sobj_list[1]), str(snew_list[1]))
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
