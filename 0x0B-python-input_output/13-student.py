#!/usr/bin/python3
"""student class module"""


class Student:
    """
    Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and hasattr(self, '__dict__'):
            ret_dict = {}
            for attr in attrs:
                if attr in self.__dict__ and type(attr) is str:
                    ret_dict[attr] = self.__dict__[attr]
            return(ret_dict)
        else:
            return(self.__dict__.copy())

    def reload_from_json(self, json):
        for k, v in json.items():
            self.__dict__[k] = v
