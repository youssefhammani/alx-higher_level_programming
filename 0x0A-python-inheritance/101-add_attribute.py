#!/usr/bin/python3
""" adds a new attribute to an object """


def add_attribute(obj, new_attr, value):
    """ add attribute """
    def add_attribute(obj, attribute, value):
        if hasattr(obj, '__dict__') or hasattr(obj, '__slots__')
        or hasattr(type(obj), '__dict__'):
            setattr(obj, attribute, value)
        else:
            raise TypeError("can't add new attribute")
