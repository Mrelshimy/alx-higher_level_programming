#!/usr/bin/python3
"""module for multiplication of 2 matrices"""


def matrix_mul(m_a, m_b):
    """ Function to multiply 2 matrices

        Args:
            m_a: first matrix
            m_b: second matrix

        Raises:
            TypeError: Raise if m_a or m_b are not lists
            TypeError: Raise if m_a or m_b are not list of lists
            ValueError: if m_a or m_b is empty matrix
            TypeError: if matrices contains other than ints or floats
            TypeError: if matrices are not rectangle
            ValueError: if matrices can't be multipied

        Return:
            multiplication result matrix

    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("Each row of m_a must be of the same size")
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if len(row) != len(m_a[0]):
            raise TypeError("Each row of m_b must be of the same size")
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[] for i in range(len(m_a))]
    for n in range(len(m_a)):
        for m in range(len(m_b[0])):
            x = 0
            for o in range(len(m_b)):
                x += m_a[n][o] * m_b[o][m]
            result[n].append(x)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
