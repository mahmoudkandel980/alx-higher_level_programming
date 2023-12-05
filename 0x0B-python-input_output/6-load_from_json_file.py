#!/usr/bin/python3

"""
This module contains a function that creates a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.
    
    Args:
        filename (str): The name of the JSON file.
    
    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename) as f:
        return json.load(f)
