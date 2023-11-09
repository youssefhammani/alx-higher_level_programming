#!/usr/bin/python3
""" return class or inherit from class """


def is_kind_of_class(obj, a_class):
    """ return class or inherit from class """
    return type(obj) is a_class or issubclass(type(obj), a_class)
