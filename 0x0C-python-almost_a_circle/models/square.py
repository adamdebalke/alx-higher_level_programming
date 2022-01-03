#!/usr/bin/python3
# square.py
"""
Defines a class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square using Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string info about this square."""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Size of this square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates attributes of the Square
        Args:
            args (non-keyword arguments): non-specified amount of arguments
            kwargs (key-word arguments): non-specified amount of arguments
        """

        attrs = ["id", "size", "x", "y"]

        for pos, val in enumerate(args):
            if pos < len(attrs):
                setattr(self, attrs[pos], val)

        if len(args) == 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the instance
        """

        new_dict = {}
        attrs = ["id", "size", "x", "y"]

        for att in attrs:
            new_dict[att] = getattr(self, att)

        return new_dict
