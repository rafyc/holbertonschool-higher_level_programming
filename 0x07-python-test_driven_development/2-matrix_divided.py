#!/usr/bin/bash

def matrix_divided(matrix, div):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = matrix[i].copy
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] / div
    return new_matrix
