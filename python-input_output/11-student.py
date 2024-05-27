#!/usr/bin/python3
"""student"""


class Student:
    """student"""

    def __init__(self, first_name, last_name, age):
        """student

        Args:
            first_name: first student name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """student to json

        Args:
            self: instance
            attrs: attributes
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """reload from json

        Args:
            json: the value to replace with
        """
        for k, v in json.items():
            setattr(self, k, v)
