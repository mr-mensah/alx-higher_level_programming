#!/usr/bin/python3
"""1function that writes to a file"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as e:
        data = e.write(text)

    return data
