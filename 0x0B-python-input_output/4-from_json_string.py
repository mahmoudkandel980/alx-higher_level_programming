#!/usr/bin/python3

"""
Module that contains a function that returns an object
represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    function that returns an object
    represented by a JSON string
    
    Args:
        my_str: JSON string
    Returns:
        object
    """
    return json.loads(my_str)
