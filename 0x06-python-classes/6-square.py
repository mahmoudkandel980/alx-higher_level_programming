#!/usr/bin/python3
"""Create a Class Square with size, area, getters and setters"""


class Square:
    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor of a size Square"""
        self.size = size
        self.position = position

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
            for blank in range(self.position[1]):
                print()
            for rows in range(self.__size):
                print(" " * self.position[0], end='')
                print("#" * self.__size)

    @property
    def position(self):
        """Getter Position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter position"""
        if len(value) != 2 or type(value) is not tuple or type(value[0]) is not int or type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
