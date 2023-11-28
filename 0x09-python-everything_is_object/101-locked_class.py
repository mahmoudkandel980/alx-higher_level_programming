#!/usr/bin/python3
"""prevents dynamic attributes creation class"""

class LockedClass():
    """Class to dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init"""
        pass
