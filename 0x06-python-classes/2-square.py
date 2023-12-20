#!/usr/bin/python3
'''This class defines a square as shown below'''


class Square:
    '''defines the new square'''
    def __init__(self, size=0):

        '''This initializes the new square
        Args:
        size(int): The size of the new square
        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
