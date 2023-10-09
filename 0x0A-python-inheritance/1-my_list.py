#!/usr/bin/python3
"""List and class """


class MyList(list):
    """list is called by class """

    def print_sorted(self):
        """print sorted list"""
        self.sort()
        print(self)
