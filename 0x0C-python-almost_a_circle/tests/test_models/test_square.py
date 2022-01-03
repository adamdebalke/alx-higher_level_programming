#!/usr/bin/python3
# test_square.py
"""
Unittests for models/square.py.
"""
import io
import sys
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Unit tests for the Square class.
    """

    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

# ---------- task 2 ---------------------------------------------

    def test_1_inheritance(self):
        """Tests if Square inherits Base & Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_2_isinstance(self):
        """make instance"""
        s = Square(2)
        self.assertTrue(isinstance(s, Base))
        self.assertTrue(isinstance(s, Rectangle))

    def test_3_class(self):
        """Tests Square class type."""
        self.assertEqual(str(Square),
                        "<class 'models.square.Square'>")

    def test_4_id(self):
        """Prints out the id"""
        s1 = Square(1, 2)
        self.assertEqual(s1.id, 1)

        s2 = Square(1, 4)
        self.assertEqual(s2.id, 2)

        s3 = Square(1, 2, 0, 12)
        self.assertEqual(s3.id, 12)
        self.assertTrue(type(s3), Square)

    def test_5_no_args(self):
        """Tests no arguments."""
        with self.assertRaises(TypeError) as e:
            s = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_6_many_args(self):
        """Tests many arguments."""
        with self.assertRaises(TypeError) as e:
            s = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 were \
given"
        self.assertEqual(str(e.exception), s)

    def test_7_size(self):
        """ Test correct size being set"""

        s1 = Square(2, 2)
        s2 = Square(98, 2)

        self.assertEqual(s1.size, 2)
        self.assertEqual(s2.size, 98)

    def test_8_type_int(self):
        """Tests type integer."""
        r = Square(10)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
            '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Square("1")
        s = "width must be an integer"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        s = "x must be an integer"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")
        s = "y must be an integer"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

    def test_9_instantiation(self):
        """Tests positional instantiation."""
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
            '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
            '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(r.__dict__, d)

    def test_10_keyword(self):
        """Tests positional instantiation."""
        r = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 100, '_Rectangle__width': 100,
            '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_11_id_inherited(self):
        """Tests if id is inherited from Base."""
        Base._Base__nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)

    def test_12_properties(self):
        """Tests property getters/setters."""
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 98, '_Rectangle__width': 98,
            '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.size, 98)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)

# ---------- task 3 ---------------------------------------------

    def invalid_types(self):
        """Returns tuple of types for validation."""
        t = (3.14, -1.1, float('Nan'), float('-inf'), True, "hello", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_13_validate_type(self):
        """Tests property validation."""
        r = Square(1)
        attributes = ["x", "y"]
        for each in attributes:
            s = "{} must be an integer".format(each)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, each, invalid_type)
                self.assertEqual(str(e.exception), s)
        s = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as e:
                setattr(r, "width", invalid_type)
            self.assertEqual(str(e.exception), s)

    def test_14_validate_value_negative_gt(self):
        """Tests property validation."""
        r = Square(1, 2)
        attributes = ["size"]
        for each in attributes:
            s = "width must be > 0".format(each)
            with self.assertRaises(ValueError) as e:
                setattr(r, each, -33)
            self.assertEqual(str(e.exception), s)

    def test_15_validate_value_negative_ge(self):
        """Tests property validation."""
        r = Square(1, 2)
        attributes = ["x", "y"]
        for each in attributes:
            s = "{} must be >= 0".format(each)
            with self.assertRaises(ValueError) as e:
                setattr(r, each, -33)
            self.assertEqual(str(e.exception), s)

    def test_16_validate_value_zero(self):
        """Tests property validation."""
        r = Square(1, 2)
        attributes = ["size"]
        for each in attributes:
            s = "width must be > 0".format(each)
            with self.assertRaises(ValueError) as e:
                setattr(r, each, 0)
            self.assertEqual(str(e.exception), s)

    def test_17_property(self):
        """Tests property setting/getting."""
        r = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for each in attributes:
            n = 33
            setattr(r, each, n)
            self.assertEqual(getattr(r, each), n)

    def test_18_property_range_zero(self):
        """Tests property setting/getting."""
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

# ---------- task 4 ---------------------------------------------

    def test_19_area_no_args(self):
        """Tests area() method signature."""
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_20_area(self):
        """Tests area() method compuation."""
        r = Square(6)
        self.assertEqual(r.area(), 36)

        r = Square(6, 7, 8, 9)
        self.assertEqual(r.area(), 36)

        r = Square(6, y=7, x=8, id=9)
        self.assertEqual(r.area(), 36)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as e:
            s1.size = "6"
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(ValueError) as e:
            s1.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

# ---------- tasks 5 & 7 ---------------------------------------------

    def test_21_display_no_args(self):
        """Tests display() method signature."""
        r = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_22_display(self):
        """Tests Square output"""
        output = io.StringIO()  # create StringIO Object
        sys.stdout = output  # Rediurect stdout

        s = Square(4, 3, 2, 1)
        s.display()  # call function
        display = "\n\n   ####\n   ####\n   ####\n   ####\n"

        self.assertEqual(output.getvalue(), display)

        sys.stdout = sys.__stdout__  # Reset redirect

# ---------- task 6 --------------------------------------------

    def test_23_str_no_args(self):
        """Tests __str__() method signature."""
        r = Square(1, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_24_str(self):
        """Tests __str__() method return."""
        r = Square(5)
        s = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(r), s)
        r = Square(1, 1)
        s = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(r), s)
        r = Square(3, 4, 5)
        s = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(r), s)
        r = Square(10, 20, 30, 40)
        s = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(r), s)

# ---------- tasks 8 & 9 -----------------------------

    def test_25_update_no_args(self):
        """Tests update() method signature."""
        r = Square(1, 2)
        with self.assertRaises(TypeError) as e:
            Square.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, d)

    def test_26_update_args(self):
        """Tests update() postional args."""
        r = Square(5, 2)
        d = r.__dict__.copy()

        r.update(1)
        d["id"] = 1
        self.assertEqual(r.__dict__, d)

        r.update(1, 5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(1, 5, 20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(1, 5, 20, 25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_27_update_args_bad(self):
        """Tests update() positional arg fubars."""
        r = Square(1, 2)
        d = r.__dict__.copy()

        r.update(1)
        d["id"] = 1
        self.assertEqual(r.__dict__, d)

        with self.assertRaises(ValueError) as e:
            r.update(1, -2)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(1, 2, -3)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(1, 2, 3, -4)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

    def test_28_update_kwargs(self):
        """Tests update() keyword args."""
        r = Square(1, 2)
        d = r.__dict__.copy()

        r.update(id=1)
        d["id"] = 1
        self.assertEqual(r.__dict__, d)

        r.update(size=2)
        d["_Rectangle__height"] = 2
        d["_Rectangle__width"] = 2
        self.assertEqual(r.__dict__, d)

        r.update(x=3)
        d["_Rectangle__x"] = 3
        self.assertEqual(r.__dict__, d)

        r.update(y=4)
        d["_Rectangle__y"] = 4
        self.assertEqual(r.__dict__, d)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

# ---------- task 14 ----------------------------------

    def test_29_to_dictionary(self):
        """Tests to_dictionary() signature:"""
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r = Square(1)
        d = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(r.to_dictionary(), d)

        r = Square(1, 2, 3, 4)
        d = {'x': 2, 'y': 3, 'size': 1, 'id': 4}
        self.assertEqual(r.to_dictionary(), d)

        r.x = 10
        r.y = 20
        r.size = 30
        d = {'x': 10, 'y': 20, 'size': 30, 'id': 4}
        self.assertEqual(r.to_dictionary(), d)

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

if __name__ == "__main__":
    unittest.main()
