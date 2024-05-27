#!/usr/bin/python3
"""read"""


def read_file(filename=""):
    """read and print"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
