#!/usr/bin/python3
"""function on JSON string """
import json
"""module to use json"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an object"""

    return json.dumps(my_obj)

