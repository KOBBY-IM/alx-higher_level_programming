#!/usr/bin/python3
"""
Module 7-base_geometry

Contains BaseGeometry
with public instance method area and integer_validation
"""


class BaseGeometry:
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates input
        Args:
            name (str): assumed always a string
            value (int): greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
