#!/usr/bin/python3

"""Define class Square with private attribute size"""


class Square:
    """
    Represent a square

    Args:
        size (int): size of a side in a square
    """
    def __init__(self, size):
        """
        initialize square

        Attributes:
            size: size of a side in a sqaure
        """
        self.__size = size
