#!/usr/bin/python3
"""
Define a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    Methods:
        __init__(self, width, height)
    """

    def __init__(self, width, height):
        """
        initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
