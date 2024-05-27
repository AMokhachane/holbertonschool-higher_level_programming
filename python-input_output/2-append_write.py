#!/usr/bin/python3
"""append"""


def append_write(filename="", text=""):
    """append

    Args:
        filename: name of file
        text: text to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
