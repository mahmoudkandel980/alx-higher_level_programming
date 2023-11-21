#!/usr/bin/python3
"""Create a Class Square with size, area, getters and setters"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Constructor of a size Square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method to get the Square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter of the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the private size attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Method to print a Square"""
        if self.__size == 0:
            print()
        else:
            for rows in range(self.__size):
                print("#" * self.__size)
