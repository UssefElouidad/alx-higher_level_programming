#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = []
    for row in matrix:
        sqred_row = []
        for element in row:
            sqred_row.append(element ** 2)
        sqr.append(sqred_row)
    return sqr
