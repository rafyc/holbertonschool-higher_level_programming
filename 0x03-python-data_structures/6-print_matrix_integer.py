#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for elements in matrix:
        for numbers in elements:
            print("{:d}".format(numbers),
                  end=" " if numbers != elements[-1] else "")
        print()
