#!/usr/bin/python3
"""Module for the Base class."""


class Base:
    """Base class for managing id attribute."""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class."""
        if id is not None:
            # Assign the public instance attribute id with the provided value
            self.id = id
        else:
            # Increment __nb_objects and assign the new value to id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
