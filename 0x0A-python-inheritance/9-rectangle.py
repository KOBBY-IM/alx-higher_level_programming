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

    def area(self):
        """
        claculate the area of the rectangle

        Returns: The area of the rectangle (int)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Get a string representation of the rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
