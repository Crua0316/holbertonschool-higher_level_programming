#!/usr/bin/python3
"""Pascal triangle in python
"""


def pascal_triangle(n):
    """creatign pascals triangle
    Args:
        n: input number of height of triangle
    Return:
        list of tirangle or empty list when n is lower and equal to 0
    """
    if n <= 0:
        return list()
    new = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(1, i):
            tmp.append(new[i - 1][j - 1] + new[i - 1][j])
        tmp.append(1)
        new.append(tmp)
    return new
