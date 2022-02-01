#!/usr/bin/python3
"""
This is module base.py
It defines a basic class Base
"""
import json
import csv


class Base:
    """
    This class Base takes one argument.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiate a Base object
        Args:
            id: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Turns the dictionary representation of an instance into JSON
        Args:
            list_dictionaries (list): list of representations of an instances
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the Python version of a JSON string
        Args:
            json_string (str): string to turn into Python object
        """

        if json_string is None or len(json_string) == 0:
            json_string = "[]"

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list of objects): list of instances who inherits of Base
        """

        filename = "{}.json".format(cls.__name__)
        my_list = []

        if list_objs is not None:
            for each in list_objs:
                my_list.append(each.to_dictionary())

        json_list = cls.to_json_string(my_list)

        with open(filename, "w+", encoding="UTF-8") as f:
            f.write(json_list)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all attributes already set
        Args:
            dictionary (dict): dictionary of values to make into an instance
        """

        if "size" in dictionary:
            new = cls(1)
        else:
            new = cls(1, 1)

        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """

        from_filename = "{}.json".format(cls.__name__)
        my_list = []

        try:
            with open(from_filename, mode="r+", encoding="UTF-8") as f:
                raw_json = f.read()
            list_output = cls.from_json_string(raw_json)
            for each in list_output:
                my_list.append(cls.create(**each))
        except FileNotFoundError:
            pass
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save information into a csv file """
        file_name = cls.__name__ + ".csv"
        with open(file_name, 'w', newline='') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    headers = ["id", "width", "height", "x", "y"]
                else:
                    headers = ["id", "size", "x", "y"]
                new_csv = csv.DictWriter(f, fieldnames=headers)
                for each in list_objs:
                    new_csv.writerow(each.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load csv data """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, 'r', newline='') as f:
                if cls.__name__ == "Rectangle":
                    headers = ["id", "width", "height", "x", "y"]
                else:
                    headers = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(f, fieldnames=headers)
                dict_list = [dict([key, int(value)] for key,
                                  value in f.items())
                             for f in dict_list]
                return [cls.create(**argument) for argument in dict_list]
        except IOError:
            return []
