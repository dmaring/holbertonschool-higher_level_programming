#!/usr/bin/python3


def delete_at(my_list=[], idx=[]):
    """Deletes an item at the specified index number"""
    if len(my_list) < 0 or (idx > len(my_list) - 1):
        return(my_list)

    for myidx, val in enumerate(my_list):
        if idx is myidx:
            del my_list[idx]

    return(my_list)
