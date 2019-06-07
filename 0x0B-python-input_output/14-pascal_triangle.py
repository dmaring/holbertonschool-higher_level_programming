#!/usr/bin/python3
"""module for pascal's triangle"""


def pascal_triangle(n):
    if n <= 0:
        return([])

    plist = []
    if n > 1:
        for r in range(n):
            plist.append(get_row(r))

    return(plist)


def get_row(n):
    rowstr = (str(11 ** n))
    return([num for num in rowstr])
