#!/usr/bin/python3
""" This module creates a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal's triangle of n
Returns an empty list if n <= 0
It can be assumed that n will be always an integer
It is not allowed to import any module """


def pascal_triangle(n):
    """ Returns a list of lists of integers
    representing Pascal's triangle of n """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
        triangle.append(row)
    return triangle
