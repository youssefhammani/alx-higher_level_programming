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

    @property
    def size(self):
        """ Getting the size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting the size of square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return current square area """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
