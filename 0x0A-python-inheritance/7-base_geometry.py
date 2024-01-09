#!/usr/bin/python3
"""Defines a class BaseGeometry"""

class BaseGeometry
"""Represent class base geometry"""

def area(self):
    """Not implemented"""
    raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """Validates a parameter as an integer.

    Args:
    name (str): The name of the parameter.
    value (int): The parameter to validate.
    Raises:
    TypeError: if value is not an integer.
    ValueError: if value is <= 0.
    """
    if type(value) != int:
        raise TypeError("<name> must be an integer")
    if type(value) <= 0:
        raise ValueError("<name> must be greater than 0")
