#!/usr/bin/python3
"""
Print a square module
"""


def print_square(size):
    """Function that prints a square with the character #"""

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for item in range(size):
        for row in range(size):
            print('#', end='')
        print()
