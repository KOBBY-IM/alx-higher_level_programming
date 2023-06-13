#!/usr/bin/python3
"""
A class MyInt that inherits from int
"""


class MyInt(int):
    """
    A rebellious interger class that inverts the behaviour of
    the equality operators == and !=
    """

    def __eq__(self, other):
        """
        Inverts the behaviour of the '==' operator.

        args
        other: The object to compare against.
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Inverts the behaviour of the '!=' operator.

        args:
        other: the object to compare against.
        """
        return not super().__ne__(other)
