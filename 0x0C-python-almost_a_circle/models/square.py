#!/usr/bin/python3
"""Square Class Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor

        Args:
            size: square width
            x: x shift
            y: y shift
            id: instance id

        Raises:
            TypeError: when any argument is not integer
            ValueError: when width is <=0
            ValueError: x or y < 0
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print rectangle attributes data"""
        return "[" + type(self).__name__ + "]" + " (" + str(self.id) + ") "\
            + str(self.x) + "/" + str(self.y) + " - "\
            + str(self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes"""
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dict representation of object"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
