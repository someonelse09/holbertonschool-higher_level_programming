#!/usr/bin/python3
""" This file writes a function that creates an Object from a JSON file """

import json


def load_from_json_file(filename):
    """ with statement must be used
    do not need to manage exceptions if the JSON string doe not represent an object.
    do not need to manage file permissions / exceptions """

    with open(filename, "r", encoding="utf-8") as file:
        json.load(file)
