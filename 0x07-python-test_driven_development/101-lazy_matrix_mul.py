#!/usr/bin/python3
"""
Multiply 2 matricies using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Matrix * Matrix
    Args:
        m_a:first matrix
        m_b:second matrix
    Returns:
        return m_b * m_a
    """
    return numpy.matmul(m_b, m_a)