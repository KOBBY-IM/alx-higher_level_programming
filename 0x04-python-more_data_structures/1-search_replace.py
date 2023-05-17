#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the replaced values.
    new_list = []

    # Iterate over the input list and replace
    # the search element with the replace element.
    for value in my_list:
        if value == search:
            new_list.append(replace)
        else:
            new_list.append(value)

    # Return the new list.
    return new_list
