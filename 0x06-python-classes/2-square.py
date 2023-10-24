#!/usr/bin/python3
""" Create class for defining square """


class Square:
    """ Create class for defining square """
    def __init__(self, size=0):
        """ Initialising attribute instance
        Args: size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
