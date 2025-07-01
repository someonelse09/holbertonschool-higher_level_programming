#!/usr/bin/python3
"""
Basic serialization module for converting Python dictionaries to JSON files
and deserializing JSON files back to Python dictionaries.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): A Python dictionary containing data to serialize
        filename (str): The filename of the output JSON file

    Returns:
        None
    """

    try:
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Data is not JSON serializable: {e}")

def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file to recreate a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file

    Returns:
        dict: A Python dictionary with the deserialized JSON data
    """

    try:
        with open(filename, 'r', encoding="utf-8") as file:
            json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The {filename} could not found")
    except IOError as e:
        raise IOError(f"Error happened while reading the {filename}: {e}")
