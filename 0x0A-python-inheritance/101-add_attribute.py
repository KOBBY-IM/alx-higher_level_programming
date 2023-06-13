#!/usr/bin/python3
"""
Contains function that adds new attribute to an object if possible
"""


def add_attribute(obj, attr, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
    - obj: The object to which the attribute should be added.
    - attr_name: The name of the attribute.
    - attr_value: The value of the attribute.

    Raises:
    - TypeError: If the object does not allow adding new attributes.
            The exception message will be "can't add new attribute".
    """

    if hasattr(obj, '__dict__'):
        obj.__dic__[attr_name] = attr_value
    else:
        raise TypeError("can´t add new attribute")
