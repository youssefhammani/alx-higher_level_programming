#!/usr/bin/python3
""" define student class """

class Student:
    """ define student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ convert to json """
        if attrs is None:
            return vars(self)

        serializable_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                serializable_dict[attr] = getattr(self, attr)
        return serializable_dict
