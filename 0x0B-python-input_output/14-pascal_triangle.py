#!/usr/bin/python3
"""pascal tringle in python
"""


def pascal_triangle(n):
    """
    implementation
    """
    new = []
    if n <= 0:
        return new
    for i in range(n):
        if i == 0:
            new.append([1])
        elif i == 1:
            new.append([1, 1])
        else:
            new_2 = []
            for j in range(i + 1):
                new_2.append(j)
                print(new_2)
            for j in range(i):
                new_2[0], new_2[i] = 1, 1
                new_2[j] = new[i - 1][j] + new[i - 1][j - 1]
            new.append(new_2)
    return new
