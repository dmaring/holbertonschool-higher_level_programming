#!/usr/bin/python3


def max_integer(my_list=[]):
    """Find the max integer in a list without using math builtin
    """
    if my_list is '':
        return(None)

    sorted_list = my_list[:]
    sorted_list.sort()
    return(sorted_list[-1])
