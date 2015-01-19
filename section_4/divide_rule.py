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


def find_max_subarry(A, low, high):
    if high-1 == low:
         return low, high, A[low]
    else:
        mid = (high + low)//2
        print mid
        left_low, left_high, left_sum = find_max_subarry(A, low, mid)
        print left_low, left_high, left_sum

        right_low, right_high, right_sum = find_max_subarry(A, mid, high)
        print right_low, right_high, right_sum
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        print cross_low, cross_high, cross_sum

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum

        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum

        else:
            return cross_low, cross_high, cross_sum


def problem_4_1_1():
    """
    Что Возвращает процедура find_max_subarry, когда все элементы A отрицательны
    :return:
    """

    list = [-12, -34, -2]
    # возвращает самы малый по модулю элемент
    return find_max_subarry(list, 0, len(list))



