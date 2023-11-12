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

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign arguments to attributes."""
        attributes = ['id', 'size', 'x', 'y']

        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

        def to_dictionary(self):
            """Return the dictionary representation of a Square."""
            return {
                    'id': self.id,
                    'size': self.width,
                    'x': self.x,
                    'y': self.y
            }
