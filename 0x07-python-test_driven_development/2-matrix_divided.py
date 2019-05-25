#!/usr/bin/python3
"""
Divide a matrix module
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix and ret a new matrix"""

    lol_error = "matrix must be a matrix (list of lists) of integers/floats"
    size_error = "Each row of the matrix must have the same size"

    if not isinstance(matrix, type([])):
        raise TypeError(lol_error)

    row_length = len(matrix[0])
    for list in matrix:
        if len(list) != row_length:
            raise TypeError(size_error)

    for list in matrix:
        for item in list:
            if not isinstance(item, (float, int)):
                raise TypeError(lol_error)
            if any([item == float('inf'), item == float('nan')]):
                raise TypeError(lol_error)

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == float('inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return([[round((item / div), 2) for item in row] for row in matrix])
