#!/usr/bin/python3
"""
This module contains the Base class
"""
import json



class Base():
    """Class that represents Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Method to initiate an object instance of Base"""
        self.id = id

    @staticmethod
    def reset_id():
        """Method that resets Base private attribute __nb_objects to 0"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that takes a list of dictionaries and returns
        the JSON string representation of 'list_dictionaries'
        """

        if not list_dictionaries or list_dictionaries == None:
            return([])
        else:
            ret_str = json.dumps(list_dictionaries, sort_keys=True)
        return(ret_str)


    @staticmethod
    def from_json_string(json_string):
        """
        Method that returns a list of the JSON string representation
        json_string: string representing a list of dictionaries
        """
        if not json_string or json_string == None or json_string == '[]':
            return([])
        else:
            return(json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that saves a list of dictionary objects
        as json file
        """

        data = []
        if list_objs is None:
            fpn = 'None.json'
            data = '[]'
        else:
            fpn = '{}.json'.format(list_objs[0].__class__.__name__)
            # need to create a list of dictionaries from
            # the list of object instances
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                data.append(obj_dict)
        json_data = cls.to_json_string(data)
        with open(fpn, 'w', encoding="utf-8") as fp:
            fp.write(json_data)

    @classmethod
    def create(cls, **dictionary):
        """Method that creates an instance from a dictionary"""
        # print(cls)
        # print("Dir of cls is: {}".format(dir(cls)))
        # print("__dict__ of cls is {}".format(cls.__dict__))
        r1 = cls(1, 2, 3, 4)
        r1.update(**dictionary)
        return(r1)

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
