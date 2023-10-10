#!/usr/bin/python3
"""function that sendstudent to JSON """


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializing of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary"""
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age,
            }
        else:
            j_dict = {}
            for i in attrs:
                j_dict[i] = getattr(self, i)
        return j_dict

    def reload_from_json(self, json):
        """function"""
        for i, value in json.items():
            setattr(self, i, value)

