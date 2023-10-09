#!/usr/bin/python3
"""function for Lookup"""


def lookup(obj):
    """
    function to return the list of available attributes

    Args:
    obj : object to get the methods and attributes for

    Return:
    list of strings containing name of attribute
    """

    return dir(obj)
