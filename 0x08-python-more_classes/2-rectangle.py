#!/usr/bin/python3
"""a Rectangle class."""


class Rectangle:
    """a rectangle"""

    def __init__(self, width=0, height=0):
        """
        the class Rectangle
        Args:
            - width: int
            - heigth: int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set rectangle width"""
        return self.__width

    @property
    def height(self):
        """Get/set the rectangle height"""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get the Rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Get the Rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))
