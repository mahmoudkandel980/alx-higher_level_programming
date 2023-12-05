#!/usr/bin/python3

"""
This module defines a function that writes an object
to a text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation
    Args:
        my_obj: object
        filename: text file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
