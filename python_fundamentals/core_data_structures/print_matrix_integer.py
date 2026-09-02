#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Args:
        matrix (list of list of int): The matrix to print.
    """
    for row in matrix:
        for idx, integer in enumerate(row):
            if idx == len(row) - 1:
                print("{}".format(integer), end="")
            else:
                print("{:d}".format(integer), end=" ")
        print()
