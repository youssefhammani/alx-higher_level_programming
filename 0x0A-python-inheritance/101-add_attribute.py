#!/usr/bin/python3
""" adds a new attribute to an object """


def add_attribute(obj, new_attr, value):
    """ add attribute """
    def add_attribute(obj, attribute, value):
        allowed_types = (dict, list, set, frozenset, tuple)
    if any(isinstance(obj, t) for t in allowed_types)
    or hasattr(type(obj), '__slots__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
