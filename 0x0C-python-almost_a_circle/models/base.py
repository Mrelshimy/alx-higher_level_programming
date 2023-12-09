#!/usr/bin/python3
"""Base Class Module"""
import json
import csv

class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
        
        Args:
            id: instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list of dicts to json representation"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of object using json rep to a file"""
        new_list =[]
        if list_objs is not None:
            for obj in list_objs:
                obj = obj.to_dictionary()
                new_list.append(obj)
        j_dict = cls.to_json_string(new_list)
        with open("{}.json".format(cls.__name__), "w", encoding='utf-8') as fp:
            fp.write(j_dict)

    @staticmethod
    def from_json_string(list_dictionaries):
        """Convert json string to list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.loads(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """create a new instance with all attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square
        
        if cls == Rectangle:
            obj = Rectangle(1, 1)
        elif cls == Square:
            obj = Square(1)
        else:
            obj = None
        if obj is not None: 
            obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Create instances from json file"""
        with open("{}.json".format(cls.__name__), encoding='utf-8') as fp:
            data = fp.read()
        if data is None or fp is None:
            return []
        else:
            dlist = Base.from_json_string(data)
        inst_list = []
        for obj_dict in dlist:
            obj = cls.create(**obj_dict)
            inst_list.append(obj)
        return inst_list
