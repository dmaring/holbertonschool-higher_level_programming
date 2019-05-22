#!/usr/bin/python3


class Node:
    """Class that defines a Node"""

    def __init__(self, data, next_node=None):
        """Initiate an instance of the Square class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__size = value

    @property
    def next_node(self):
        """Get the next_node attribute of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node attribute of the node"""
        if (type(value) != Node and value is not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__position = value


class SinglyLinkedList:
    """Class that defines a Node"""

    def __init__(self):
        self.__head

    def sorted_insert(self, value):
            pass
