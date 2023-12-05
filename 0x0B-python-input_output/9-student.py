#!/usr/bin/python3

"""JSON representation of an object."""


class Student:
    """Defines a student."""


    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student.

        Returns:
            dict: The dictionary representation of the object.
        """
        return self.__dict__
