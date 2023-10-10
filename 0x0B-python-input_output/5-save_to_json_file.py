#!/usr/bin/python3

"""function that saves object to file """
import json


def save_to_json_file(my_obj, filename):
    """
    sends an Object to a text file.
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)

