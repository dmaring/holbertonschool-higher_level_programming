#!/usr/bin/python3


def common_elements(set_1, set_2):
    myset = set()
    for i in set_1:
        for j in set_2:
            if i is j:
                myset.add(i)
    return(myset)
