#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            break
        i += 1

    print("")
    return i


"""
def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        idx += 1
    print("")
    return idx
"""
