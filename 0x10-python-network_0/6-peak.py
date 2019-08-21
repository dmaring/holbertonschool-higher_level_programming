#!/usr/bin/python3
"""
A python script that finds a peak in a list of integers.
"""


def find_peak(list_of_integers):
    """
    A python script that finds a peak in a list of integers.
    """

    list_len = len(list_of_integers)
    if list_len == 0:
        return(None)

    for idx, _num in enumerate(list_of_integers):
        if idx == 0:
            if list_of_integers[1] <= _num:
                return (_num)
        elif idx == list_len - 1:
            if list_of_integers[list_len - 2] <= _num:
                return (_num)
        else:
            if list_of_integers[idx] >= list_of_integers[idx - 1] and
            list_of_integers[idx] >= list_of_integers[idx + 1]:
                return (_num)
