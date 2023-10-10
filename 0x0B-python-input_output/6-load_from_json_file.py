#!/usr/bin/python3
"""function that loads from json"""
import json


def load_from_json_file(filename):
    """loads from json to file"""
    with open(filename, encoding="utf-8") as load:
        return json.load(load)

