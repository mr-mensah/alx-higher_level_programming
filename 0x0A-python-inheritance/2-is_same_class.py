#!/usr/bin/python3
"""Fuction that returns specific class"""


def is_same_class(obj, a_class):
    """function that checks if an object is an instance of a given class"""
    if type(obj) == a_class:
        return True
    return False
