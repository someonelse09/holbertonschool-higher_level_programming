#!/usr/bin/python3

import json
import csv


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        with open('data.json', "w") as file:
            json.dump(data, file, indent=4)
        return True
    except:
        return False
