#!/usr/bin/python3

"""
Defines class Square with private size and public area
able to access and update size
"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side in square

    Functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
    """

    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
        """
        self.size = size

    @property
    def size(self):
        """"
        Get the current size of the sqaure

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the current size of the sqaure

        Args:
            value: sets size to value, if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of the square
        Returns:
            area of the sqaure
        """
        return (self.__size)**2
