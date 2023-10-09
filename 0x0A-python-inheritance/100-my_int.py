#!/usr/bin/python3
"""inhertance of int"""


class MyInt(int):
    """MyInt that inherits from int"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
