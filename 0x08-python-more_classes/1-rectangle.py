#!/usr/bin/python3

class Rectangle:
    '''Defines a rectangle'''

    def __init__(self, width=0, height=0):

        '''
        This initializes an instance of the rectangle class

        Args:
        width: the widt of the rectangle is equivalent to 0

        '''

        @property
        def width(self):

            '''
            retrieves the property

            '''
            return self._width
        '''width setter'''
        @width.setter
        def width(self, value):
            self._width = width
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")

            '''For private attribute height'''
            def __init__(self, height=0):

                '''
                Start of new attribute

                '''

            @property
            def height(self):
                '''
                The getter method for the height attribute

                Returns the height of the rectangle

                '''
                return self._height

            @height.setter
            def height(height, int):
                '''
                The setter method for the height of the rectangle

                Args:
                Value(int): The new height of the rectangle

                '''
                if not isinstance(height, int):
                    raise TypeError("height must be an integer")
                if height < 0:
                    raise ValueError("height must be >=")

                self._height = height
