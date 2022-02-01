#!/usr/bin/python3
# rectangle.py
"""
Defines a class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle using Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): the x coordinate of the new Rectangle.
            y (int): the y coordinate of the new Rectangle.
            id (int): Id of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def integer_validator(var_name, value):
        """ Validates and handles all error messages
        Args:
            var_name (str): the variable name
            value (int): the value associated with var_name
        """

        wh = ["width", "height"]
        xy = ["x", "y"]

        if type(value) != int:
            raise TypeError("{} must be an integer".format(var_name))
        if var_name in wh and value <= 0:
            raise ValueError("{} must be > 0".format(var_name))
        if var_name in xy and value < 0:
            raise ValueError("{} must be >= 0".format(var_name))

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        Args:
            value (int): the width to set
        """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        Args:
            value (int): the height to set
        """
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x
        Args:
            value (int): the value to assign to x
        """

        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y
        Args:
            value (int): the value to assign to y
        """
        self.integer_validator("y", value)
        self.__y = value

    def area(self):
        """Returns the area of this rectangle."""
        return (self.width * self.height)

    def display(self):
        """
        Returns string representation of Rectangle
        """
        print("\n"*self.y, end="")
        for _ in range(self.height):
            print(" "*self.x + "#"*self.width)

    def __str__(self):
        """
        Returns the representation of Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y,
                    self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Updates attributes of the Rectangle
        Args:
            args (non-keyword arguments): non-specified amount of arguments
            kwargs (key-word arguments): non-specified amount of arguments
        """

        attrs = ["id", "width", "height", "x", "y"]

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
        attrs = ["id", "width", "height", "x", "y"]

        for att in attrs:
            new_dict[att] = getattr(self, att)

        return new_dict
