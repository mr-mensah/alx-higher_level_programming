#!/usr/bin/python3
"""function from the JSON string to Object"""
import json
"""from the json module"""


def from_json_string(my_str):
    """function that returns an object represented by a JSON string
    """

    return json.loads(my_str)
