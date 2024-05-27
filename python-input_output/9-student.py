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

    def to_json(self):
        """student to json"""
        return self.__dict__
