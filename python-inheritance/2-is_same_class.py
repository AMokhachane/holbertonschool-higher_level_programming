#!/usr/bin/python3
"""same_class"""


def is_same_class(obj, a_class):
    """same_class

    Args:
        obj: object to check
        a_class: class to check against
    """
    if type(obj) is a_class:
        return True
    return False
