#!/usr/bin/python3
"""Class Rectangle module"""


class Rectangle:
    """
    Class to define Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor

        Args:
            width: rectangle width
            height: rectangle height

        Raises:
            TypeError: height or width not int
            ValueError: height or width < 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """heigth setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method to return rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """Method to return rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.width + self.height))

    def __str__(self):
        """print rectangle with # sign"""
        result = ""
        if self.height == 0 or self.width == 0:
            return result
        else:
            for i in range(self.height):
                for j in range(self.width):
                    result += str(self.print_symbol)
                result += "\n"
            result = result[:-1]
            return result

    def __repr__(self):
        """return string representation of rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """delete instance method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare 2 rectangles based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
