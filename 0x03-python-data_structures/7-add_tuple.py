#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """Returns a tuple where the first element should be the addition of the
    first element of each argument. The second element should be the addition of
    the second element of each argument
    """
    if len(tuple_a) == 2:
        a1, a2 = tuple_a[0], tuple_a[1]
    if len(tuple_b) == 2:
        b1, b2 = tuple_b[0], tuple_b[1]
    if len(tuple_a) == 1:
        a1 = tuple_a[0]
        a2 = 0
    if len(tuple_b) == 1:
        b1 = tuple_b[0]
        b2 = 0
    if len(tuple_a) == 0:
        a1, a2 = 0, 0
    if len(tuple_b) == 0:
        b1, b2 = 0, 0
    ret_tup = (a1 + b1, a2 + b2)
    return(ret_tup)
