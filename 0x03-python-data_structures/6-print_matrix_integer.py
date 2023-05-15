#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for i in row:
            if i is not row[len(row) - 1]:
                print("{}".format(i), end=" ")
            else:
                print("{}".format(i), end=" ")
        print()
