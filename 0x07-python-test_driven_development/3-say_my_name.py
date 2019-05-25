#!/usr/bin/python3
"""
Divide a matrix module
"""


def say_my_name(first_name, last_name=""):
    """Function that divides all elements of a matrix and ret a new matrix"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "":
        print("My name is {}".format(first_name, last_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
