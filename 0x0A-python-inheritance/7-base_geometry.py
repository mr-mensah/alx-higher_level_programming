#!/usr/bin/python3
"""Geometry"""


class BaseGeometry:
    """geometry module """

    def area(self):
        """function not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
