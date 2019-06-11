#!/usr/bin/python3
import json
"""
This module contains the Base class
"""


class Base():
    """Class that represents Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Method to initiate an object instance of Base"""
        self.id = id

    def to_json_string(list_dictionaries):
        """
        Method that takes a list of dictionaries and returns
        the JSON string representation of 'list_dictionaries'
        """

        if not list_dictionaries or list_dictionaries == None:
            return([])
        else:
            ret_str = json.dumps(list_dictionaries)
        return(ret_str)

    @staticmethod
    def reset_id():
        Base.__nb_objects = 0

    @property
    def id(self):
        """Method to get the value of id"""
        return (self.__id)

    @id.setter
    def id(self, value):
        """Method to set the value of id"""
        if value is None:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
        else:
            self.__id = value
