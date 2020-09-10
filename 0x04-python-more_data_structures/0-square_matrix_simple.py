#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for b in matrix:
        n_matrix += [list(map((lambda x: x * x), b))]
    return n_matrix
