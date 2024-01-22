#!/usr/bin/python3
""" A module for rotating an nxn 2D matrix 90 degrees clockwise """


def rotate_2d_matrix(matrix):
    """
    Rotate a 2d square matrix 90 degrees clockwise
    Args:
        matrix (list): 2d square matrix
    Return:
        None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(n):
        for j in range(int(n / 2)):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = tmp
