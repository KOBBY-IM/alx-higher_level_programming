#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values.
    new_dictionary = {}

    # Iterate over the keys and values in the dictionary.
    for key, value in a_dictionary.items():
        # Multiply the value by 2.
        new_value = value * 2

        # Add the new key and value to the new dictionary.
        new_dictionary[key] = new_value

    # Return the new dictionary.
    return new_dictionary
