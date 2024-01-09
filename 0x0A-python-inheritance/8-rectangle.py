#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent Rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new rectangle.

        Args:
        Width(int): The width of the new rectangle.
        Height(int): The height of the new rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
