#!/usr/bin/python3
"""read_lines module"""


def read_lines(filename="", nb_lines=0):
    """function that returns the number of lines of a text file"""

    num = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            num += 1

    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0 or nb_lines >= num:
            for line in f:
                print(line, end='')
        else:
            for line in range(nb_lines):
                print(f.readline(), end='')
