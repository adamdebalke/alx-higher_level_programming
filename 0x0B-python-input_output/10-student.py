#!/usr/bin/python3
"""Definition of Student class"""


class Student:
    """Definition of the class Student.
    Attributes:
        first_name: The first name
        last_name: The last name
        age: the age
    Args:
        first_name: First name argument
        last_name: Last name argument
        age: Age argument
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved, otherwise all attributes
        must be retrieved.
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except Exception:
                pass
        return new_dict
