#!/usr/bin/python3
"""
Test 0x16 - Rotate 2D Matrix
"""


def print_matrix(matrix):
    """ Print matrix with new lines """
    print("=====================")
    for i in range(len(matrix)):
        print(matrix[i])


rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print_matrix(matrix)

    matrix = [[1, 2],
              [4, 5]]

    rotate_2d_matrix(matrix)
    print_matrix(matrix)

    matrix = [[1]]

    rotate_2d_matrix(matrix)
    print_matrix(matrix)

    matrix = [[1, 2, 3, 8],
              [4, 5, 6, 0],
              [7, 8, 9, 2],
              [4, 3, 2, 1]]

    rotate_2d_matrix(matrix)
    print_matrix(matrix)

    matrix = [[1, 2, 3, 8, 9],
              [4, 5, 6, 0, 7],
              [7, 8, 9, 2, 6],
              [4, 3, 2, 1, 5],
              [-2, 8, 0, -8, 4]]

    rotate_2d_matrix(matrix)
    print_matrix(matrix)
