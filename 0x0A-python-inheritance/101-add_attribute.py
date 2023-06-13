#!/usr/bin/python3
"""
Contains function that adds new attribute to an object if possible
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
    - obj: The object to which the attribute should be added.
    - attr: The name of the attribute.
    - value: The value of the attribute.

    Raises:
    - TypeError: If the object does not allow adding new attributes.
            The exception message will be "can't add new attribute".
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
        return
    raise TypeError("can't add new attribute")
