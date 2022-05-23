#!/usr/bin/python3
"""
The matrix_divided function
"""


def matrix_divided(matrix, div):
    """function that divide all number in the matric by the divider

    Args:
        matrix (list of list): several lists of int
        div (int): the divider

    Returns:
        list: a new matrix divided
    """
    if isinstance(matrix, list) is False:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        if isinstance(matrix[i], list) is False:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        size = len(matrix[0])
        if len(matrix[i]) != size:
            raise TypeError("Each row of the matrix must have the same size")

        new_matrix[i] = matrix[i].copy()

        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j], (int, float)) is False:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i][j] = round((matrix[i][j] / div), 2)
    return new_matrix
