# -*- coding: utf-8 -*-

__author__ = 'cpn'

"""
    Сортировки из главы 2
"""


def insertion_sort(array):
    """
    Функция для сортировки массива из натуральных чисел методом вставки, n^2 сложность

    @param array: входной массив целых чисел
    @type: list

    @return: выходной массив
    @rtype: list
    """
    for index, i in enumerate(array[1:], 1):
        key = i
        i = index - 1
        while i >= 0 and array[i] > key:
            array[i+1] = array[i]
            i -= 1

        array[i+1] = key

    return array


def selection_sort(array):
    """
    Функция для сортировки массива из натуральных чисел методом выбора, n^2 сложность

    @param array: входной массив целых чисел
    @type: list

    @return: выходной массив
    @rtype: list
    """

    for index, i in enumerate(array):
        f = max_i(array[index:])+index
        if i < array[f]:
            array[index], array[f] = array[f], array[index]

    return array


def max_i(array):
    """
    Нахождение index'а максимального элемента в массиве
    @param array: входной массив
    @return: индекс максимального елемента
    """
    el_max = array[0]
    index_max = 0

    for index, i in enumerate(array):
        if i > el_max:
            el_max = i
            index_max = index
    return index_max


def merge_sort(array, p, r):
    """
    Функция для сортировки массива из натуральных чисел методом слияния, ассимтотика n*lgn

    @param array: входной массив целых чисел
    @type: list

    @return: выходной массив, отсортированный.
    @rtype: list
    """
    if p < r:
        q = (p+r)//2
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        merge(array, p, q, r)

    return array


def merge(array, p, q, r):
    """
    Функция для слияния двух отсортированных массивов

    @param array: исходный массив
    @param p: индекс начала
    @param q: индекс середины
    @param r: индекс окончания
    :return: результирующий массив
    """

    left = array[p:q+1]
    right = array[q+1:r+1]

    i = 0
    j = 0

    for key in xrange(p, r+1):

        if i >= len(left) and j < len(right):
            array[key] = right[j]
            j += 1

        elif j >= len(right) and i < len(left):
            array[key] = left[i]
            i += 1

        elif j >= len(right) and i >= len(left):
            break

        elif left[i] <= right[j]:
            array[key] = left[i]
            i += 1

        else:
            array[key] = right[j]
            j += 1



if __name__ == '__main__':
    pass