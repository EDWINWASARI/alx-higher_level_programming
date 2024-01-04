#!/usr/bin/python3
'''Defines the rectangle'''


class Rectangle:
    '''Represents the rectangle'''

    def __init__(self, width=0, height=0):
        '''This initializes an instance of the rectangle class

        Args:
        width(int): the width of the rectangle is equivalent to 0
        height(int): The height of the rectangle
        '''
        self.width = width
        self.height = height

        @property
        def width(self):
            '''Sets the width of the rectangle'''
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")

            self.__width = value

            @property
            def height(self):
                '''Sets the height of the rectangle'''
                return self.__height

            @height.setter
            def height(height, value):
                if not isinstance(height, int):
                    raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")

            self.__height = value
