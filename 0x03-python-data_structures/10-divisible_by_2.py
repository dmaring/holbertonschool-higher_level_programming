#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Find all multiples of two in a list"""
    if my_list == '':
        return(None)

    new_list = my_list.copy()
    for idx, val in enumerate(new_list):
        if val % 2 is 0:
            new_list[idx] = True
        else:
            new_list[idx] = False
    return(new_list)
