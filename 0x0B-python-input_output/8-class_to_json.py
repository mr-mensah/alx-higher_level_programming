#!/usr/bin/python3
"""function that  class-to-JSON module."""


def class_to_json(obj):
    """ the dictionary represntation of json."""
    return obj.__dict__
