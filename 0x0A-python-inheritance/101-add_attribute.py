#!/usr/bin/python3
""" adds a new attribute to an object """


def add_attribute(obj, new_attr, value):
    """ add attribute """
    obj_dict = hasattr(obj, '__dict__')
    obj_slots = hasattr(obj, '__slots__')
    type_dict = hasattr(type(obj), '__dict__')

    if obj_dict or obj_slots or type_dict:
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
