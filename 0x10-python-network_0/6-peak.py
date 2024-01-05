#!/usr/bin/python3
"""has the function find_peak"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    li = list_of_integers
    i = len(li)
    if i == 0:
        return
    m = i // 2
    if (m == i - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != i - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
