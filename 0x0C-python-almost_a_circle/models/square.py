#!/usr/bin/python3
"""Module for the Square class."""
from rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the __str__ method."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
