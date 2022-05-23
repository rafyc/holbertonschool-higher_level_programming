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
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[i] = matrix[i].copy()
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round((matrix[i][j] / div), 2)
    return new_matrix
