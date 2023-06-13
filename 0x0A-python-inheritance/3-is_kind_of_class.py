#!/usr/bin/python3
"""
Defines a class and inherited class checking funntions
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, of if the object
    is an instance of a class that inhrited from the scpecified class

    Args:
        obj: The object to check.
        a_class: the class to check against.

    Returns:
        True if the object is an instance of a_class or a subclass,
        False otherwise
"""
    if isintance(obj, a_class):
        return True
    return False
