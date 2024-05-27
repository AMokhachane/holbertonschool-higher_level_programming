#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """write file

    Args:
        filename: name of file to write
        text: text to write into filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
