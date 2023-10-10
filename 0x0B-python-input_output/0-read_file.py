#!/usr/bin/python3
"""0function that reads file"""


def read_file(filename=""):
    """function that reads a text file"""

    with open(filename, encoding="utf-8") as e:
        print(e.read(), end="")
