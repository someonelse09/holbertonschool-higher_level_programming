#!/usr/bin/python3
""" a class Student that defines a student by
Public instance attributes:first_name; last_name; age. """


class Student:
    def __init__(self, first_name, last_name, age):
        """ This is the initializer method """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ This method retrieves a dictionary representation
        of a Student instance such that
        if attrs is a list of strings, only attribute names contained in this
        list must be retrieved. Otherwise, all attributes must be retrieved """

        e_dict = {}
        if not isinstance(attrs, list):
            return self.__dict__
        for k, v in self.__dict__.items():
            if k in attrs:
                e_dict[k] = v
            else:
                continue
        return e_dict

    def reload_from_json(self, json):
        """ This method replaces all attributes of the Student instance
        It can be assumed that json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute """

        self.__dict__.update(json)
