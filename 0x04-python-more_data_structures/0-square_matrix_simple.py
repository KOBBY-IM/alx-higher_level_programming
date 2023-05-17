#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Check if the input matrix is empty.
    if not matrix:
        return []

    # Create a new matrix to store the squared values.
    squared_matrix = []

    # Iterate over the input matrix and square each value.
    for row in matrix:
        squared_row = []
        for value in row:
            squared_row.append(value ** 2)
        squared_matrix.append(squared_row)

    # Return the new matrix.
    return squared_matrix
