#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Create a set to store the common elements.
    common_elements = set()

    # Iterate over the first set and add each element
    # to the set of common elements if it is also in the second set.
    for element in set_1:
        if element in set_2:
            common_elements.add(element)

    # Return the set of common elements.
    return common_elements
