# -*- coding: utf-8 -*-

__author__ = 'cpn'

"""
    глава 4. Разделяй и властвуй.
"""


def find_max_crossing_subarray(A, low, mid, high):
    """
    Максимальный подмассив, пересекающий среднюю точку
    :param A:
    :param low:
    :param mid:
    :param high:
    :return:
    """
    left_sum = None
    sum = 0
    max_left = None

    for i in reversed(xrange(mid)):
        sum = sum + A[i]
        if left_sum is None or sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = None
    sum = 0
    max_right = None

    for j in xrange(mid, high):
        sum = sum + A[j]
        if right_sum is None or sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum+right_sum
#kixbox.ru

