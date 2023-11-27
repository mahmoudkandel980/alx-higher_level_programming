#!/usr/bin/python3
"""a Rectangle class."""


class Rectangle:
    """a rectangle
    Attributes:
        instances_no (int): The number of instances of Rectangle
        print_symbol (any): string representation
    """
    
    instances_no = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        the class Rectangle
        Args:
            - width: int
            - heigth: int
        """
        type(self).instances_no += 1
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
    
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Get the greater area rectangle

        Args:
            rect_1 : The first Rectangle
            rect_2 : The second Rectangle
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
    
    def __str__(self):
        """Representation of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ("")
    
        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
    
    def __repr__(self):
        """Get representation of the Rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)
    
    def __del__(self):
        """For every deletion of a Rectangle print a message"""
        type(self).instances_no = type(self).instances_no - 1
        print("Bye rectangle...")
