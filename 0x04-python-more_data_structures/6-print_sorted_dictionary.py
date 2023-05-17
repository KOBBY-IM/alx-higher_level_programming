#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Iterate over the sorted keys and print the key and value.
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
