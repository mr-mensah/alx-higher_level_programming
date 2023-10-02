#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """A function with the definition of a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with the given width and height.

        Args:
        width (int, optional): The width of the rectangle. Defaults equals 0.
        height (int, optional): The height of the rectangle. Defaults equals 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width of the rectangle

        Returns:
        int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle

        Args:
        value (int): new width of the rectangle

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        gets the height of a rectangle

        Returns:
        int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle

        Args:
        value (int): new height of the rectangle

        Raises:
        TypeError: if height is not an integer
        ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
