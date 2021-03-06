#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """
    A function that returns the dictionary description with
    simple data structure (list, dict, string, integer
    and boolean) for JSON serialization of an object.
    """

    if hasattr(obj, '__dict__'):
        return(obj.__dict__)
