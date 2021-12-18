#!/usr/bin/python3
""" divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
        divides all elements of a matrix
        Args:
            matrix: matrix to be divided
            div: number used to divide
        Return:
            matrix with divided elements
    """
    if not all(isinstance(matrix, list)):
        raise TypeError(
            'matrix must be a matrix (list of lists)of integers/floats'
             )
    """ if all lists are of the same length """
    it = iter(matrix)
    length = len(next(it))
    if not all(len(l) == length for l in it):
        raise TypeError('Each row of the matrix must have the same size')
    """ checking for list values """
    for lst in matrix:
        for num in lst:
            if type(num) not in [int, float] or num is None:
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    ' of integers/floats'
                     )
    """ checking for div """
    if type(div) not in [int, float] or div is None:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    """ else, divide the matrix """
    return([list(map(lambda x: round(x / div, 2), num))for num in matrix])
