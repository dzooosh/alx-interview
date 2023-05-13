#!/usr/bin/python3

""" Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ rotates 2D Matrix 90 degrees clockwise
    Args:
        matrix - to be edited in-place
    """

    # get one side of the matrix
    n = len(matrix)
    # swap rows and columns
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
