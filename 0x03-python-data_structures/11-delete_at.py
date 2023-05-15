#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check for empty list.
    if not my_list:
        return []

    # Check for invalid index.
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Copy the list to a new list, without the item at
    # the specified index.
    new_list = my_list[:idx] + my_list[idx + 1:]

    # Return the new list.
    return new_list
