#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Create a set to store the elements present in only one set.
    only_diff_elements = set()

    # Iterate over the first set and add each element
    # to the set of only diff elements if it is not in the second set.
    for element in set_1:
        if element not in set_2:
            only_diff_elements.add(element)

    # Iterate over the second set and add each element to
    # the set of only diff elements if it is not in the first set.
    for element in set_2:
        if element not in set_1:
            only_diff_elements.add(element)

    # Return the set of only diff elements.
    return only_diff_elements
