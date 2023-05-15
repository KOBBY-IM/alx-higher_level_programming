#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Check for empty list.
    if not my_list:
        return []

    # Initialize a new list to store the results.
    divisible_by_2 = []

    # Iterate over the list, and add True if the
    # integer is a multiple of 2, or False otherwise.
    for integer in my_list:
        if integer % 2 == 0:
            divisible_by_2.append(True)
        else:
            divisible_by_2.append(False)

    # Return the new list.
    return divisible_by_2
