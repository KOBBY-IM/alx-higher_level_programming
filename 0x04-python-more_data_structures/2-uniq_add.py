#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create a set to store the unique integers.
    unique_integers = set()

    # Iterate over the input list and add each integer to the set.
    for integer in my_list:
        unique_integers.add(integer)

    # Sum the unique integers.
    sum_of_unique_integers = sum(unique_integers)

    # Return the sum of the unique integers.
    return sum_of_unique_integers
