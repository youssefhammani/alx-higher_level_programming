#!/usr/bin/python3
""" adds a new attribute to an object """


def add_attribute(obj, new_attr, value):
    """ add attribute """
    allowed_types = (dict, list, set, frozenset, tuple)
    is_type_allowed = any(isinstance(obj, t) for t in allowed_types)
    has_slots = hasattr(type(obj), '__slots__')

    if is_type_allowed or has_slots:
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
