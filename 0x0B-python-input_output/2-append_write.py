#!/usr/bin/python3
"""function that appends to a file"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as e:
        info = e.write(text)

    return info

