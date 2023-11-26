#!/usr/bin/python3
"""
Lazy matrix mul using Numpy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Matrix mul using Numpy

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        Result of multiplication matrix
    """
    return np.matmul(m_a, m_b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
