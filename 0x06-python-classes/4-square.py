#!/usr/bin/python3
'''defines a square'''


class Square:
    '''This is the new square'''

    def __init__(self, size=0):
        '''Initializes the new square

        Args:
        size (int): This is the size of the new square
        '''
        self.__size = size

    @property
    def size(self):
        '''Getter method to retrieve the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method to update the size

        Args:
        value (int): The new size for the square
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        '''Calculates the area of a square'''
        return self.__size ** 2
