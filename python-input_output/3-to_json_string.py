#!/usr/bin/python3
""" This module includes the function to_json_string(my_obj) """

import json


def to_json_string(my_obj):
    """ The function serves as a tool for
    converting an object into json string """

    return json.dumps(my_obj)
