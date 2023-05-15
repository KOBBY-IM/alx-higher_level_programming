#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check for empty list.
    if not my_list:
        return None

    # Initialize the biggest integer to the first element of the list.
    biggest_integer = my_list[0]

    # Iterate over the list, and update the biggest integer
    # if a larger integer is found.
    for integer in my_list:
        if integer > biggest_integer:
            biggest_integer = integer

    # Return the biggest integer.
    return biggest_integer
