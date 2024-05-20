#!/usr/bin/python3
"""rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle"""

    def __init__(self, width, height):
        """rectangle

        Args:
            self: instance
            width: width of the new triangle
            height: height of the triangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
