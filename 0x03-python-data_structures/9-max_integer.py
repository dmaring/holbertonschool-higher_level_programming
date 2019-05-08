#!/usr/bin/python3


def max_integer(my_list=[]):
    """Find the max integer in a list without using math builtin
    """
    if my_list == '':
        return(None)

    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return(max)
