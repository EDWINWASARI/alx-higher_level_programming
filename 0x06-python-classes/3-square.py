#!/usr/bin/python3
'''defines a square'''


class Square:
    '''This is the new square'''

    def __init__(self, size=0):
        '''Initializes the new square

        Args:
        size(int): This is the size of the new square
        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        '''clculates the area of a square'''
        return self.__size ** 2
