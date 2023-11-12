#!/usr/bin/python3
"""Module for the Rectangle class."""
from base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class."""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def validate_integer(self, attribute, value):
        """Validate that the value is an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))

    def validate_positive(self, attribute, value):
        """Validate that the value is greater than 0."""
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def validate_non_negative(self, attribute, value):
        """Validate that the value is greater than or equal to 0."""
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with the character #."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Override the __str__ method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args):
        """Assign arguments to attributes."""
        attributes = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            setattr(self, attributes[i], args[i])
