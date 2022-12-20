#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''
def pascal_triangle(n):
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
        elif i == 1:
            result.append([1, 1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
    return result
