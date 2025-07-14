#!/usr/bin/python3
""" This module includes a function that writes an
Object to a text file, using a JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """ with statement must be used
    do not need to manage exceptions if the object can not be serialized.
    do not need to manage file permission exceptions. """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
