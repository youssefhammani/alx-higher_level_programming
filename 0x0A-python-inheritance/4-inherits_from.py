#!/usr/bin/python3
""" to check subclass """


def inherits_from(obj, a_class):
    """ to check subclass """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
