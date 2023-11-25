#!/usr/bin/python3
"""module for dividing all items of a matrix"""


def matrix_divided(matrix, div):
    """ Function to divide all items of matrix by iput int

        Args:
            matrix: matrix to divide
            div: divident

        Raises:
            TypeError: Raise if matrix elements or div are not int or float
            TypeError: Each row of the matrix must have the same size

        Returns:
            matrix of result items
    """

    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    ln = len((matrix[0]))
    for row in matrix:
        new_row = []
        if len(row) != ln:
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
            new_row.append(round((i / div), 2))
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
