#!/usr/bin/python3
# test_rectangle.py
"""
Unittests for models/rectangle.py.
"""
import io
import sys
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unit tests for the Rectangle class.
    """

    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

# ---------- task 2 ---------------------------------------------

    def test_0_class(self):
        """Tests Rectangle class type."""
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_1_id(self):
        """Prints out the id"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 4)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(1, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertTrue(type(r3), Rectangle)

    def test_2_inheritance(self):
        """Tests if Rectangle inherits Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_3_no_args(self):
        """Tests no arguments."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_4_many_args(self):
        """Tests many arguments."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        s = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(e.exception), s)

    def test_5_one_args(self):
        """Tests one argument."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_6_isinstance(self):
        """make instance"""
        r = Rectangle(1, 2)
        self.assertTrue(isinstance(r, Base))

    def test_7_type_int(self):
        """Arguments of type integer"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle("1", 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, "3")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, "4")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -2)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -3)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -4)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_8_instantiation(self):
        """Tests positional instantiation."""
        r = Rectangle(1, 2, 3, 4)
        d = {'_Rectangle__height': 2, '_Rectangle__width': 1,
             '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Rectangle(1, 2, 3, 4, 5)
        d = {'_Rectangle__height': 2, '_Rectangle__width': 1,
             '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 5}
        self.assertEqual(r.__dict__, d)

    def test_9_keyword(self):
        """Tests positional instantiation."""
        r = Rectangle(1, 2, id=3, y=4, x=5)
        d = {'_Rectangle__height': 2, '_Rectangle__width': 1,
             '_Rectangle__x': 5, '_Rectangle__y': 4, 'id': 3}
        self.assertEqual(r.__dict__, d)

    def test_10_id_inherited(self):
        """Tests if id is inherited from Base."""
        Base._Base__nb_objects = 98
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 99)

    def test_11_properties(self):
        """Tests property getters/setters."""
        r = Rectangle(5, 9)
        r.width = 1
        r.height = 2
        r.x = 3
        r.y = 4
        d = {'_Rectangle__height': 2, '_Rectangle__width': 1,
             '_Rectangle__x': 3, '_Rectangle__y': 4, 'id': 1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

# ---------- task 3 ---------------------------------------------

    def invalid_types(self):
        """wrong types"""
        t = (3.14, -1.1, float('NaN'), float('-inf'), True, "hello", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_12_validate_type(self):
        """Test wrong types"""
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for each in attributes:
            s = "{} must be an integer".format(each)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, each, invalid_type)
                self.assertEqual(str(e.exception), s)

    def test_13_validate_value_negative_gt(self):
        """Test with negative value"""
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -33)
            self.assertEqual(str(e.exception), s)

    def test_14_validate_value_negative_ge(self):
        """Test with negative value"""
        r = Rectangle(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -33)
            self.assertEqual(str(e.exception), s)

    def test_15_validate_value_zero(self):
        """Test with 0"""
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, 0)
            self.assertEqual(str(e.exception), s)

    def test_16_property(self):
        """Tests property setting/getting."""
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = 33
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_17_property_range_zero(self):
        """Tests property setting/getting."""
        r = Rectangle(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

# ---------- task 4 ---------------------------------------------

    def test_18_area_no_args(self):
        """Tests area() method signature."""
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_19_area(self):
        """Tests area() method."""
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

        r1 = Rectangle(3, 2)
        r1.width = 2
        r1.height = 4
        self.assertEqual(r1.area(), 8)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(height=8, width=7, x=0, y=0, id=12)
        self.assertEqual(r3.area(), 56)

        with self.assertRaises(TypeError) as e:
            Rectangle.area(self, "Hello")
        s = "area() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), s)

# ---------- tasks 5 & 7 -----------------------------

    def test_20_display(self):
        """Tests rectangle output"""
        output = io.StringIO()  # create StringIO Object
        sys.stdout = output  # Redirect stdout

        r = Rectangle(2, 2, 2, 2)
        r.display()  # call function
        display = "\n\n  ##\n  ##\n"
        self.assertEqual(output.getvalue(), display)

        r = Rectangle(2, 2)
        r.display()  # call function
        display = "\n\n  ##\n  ##\n##\n##\n"
        self.assertEqual(output.getvalue(), display)

        sys.stdout = sys.__stdout__  # Reset redirect

    def test_21_display_no_args(self):
        """Tests display() method signature."""
        r = Rectangle(9, 8)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        s = "display() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            Rectangle.display(self, 9)
        self.assertEqual(str(e.exception), s)

# ---------- task 6 --------------------------------------------

    def test_22_str_no_args(self):
        """__str__()"""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_23_str(self):
        """__str__()"""
        r = Rectangle(5, 5, 1)
        s = '[Rectangle] (1) 1/0 - 5/5'
        self.assertEqual(str(r), s)

        r = Rectangle(4, 6, 2, 1, 12)
        s = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(str(r), s)

        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

# ---------- tasks 8 & 9 -----------------------------

    def test_24_update_no_args(self):
        """Tests update() method signature."""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, d)

    def test_25_update_args(self):
        """Tests update() postional args."""
        r = Rectangle(5, 2)
        d = r.__dict__.copy()

        r.update(1)
        d["id"] = 1
        self.assertEqual(r.__dict__, d)

        r.update(1, 2)
        d["_Rectangle__width"] = 2
        self.assertEqual(r.__dict__, d)

        r.update(1, 2, 3)
        d["_Rectangle__height"] = 3
        self.assertEqual(r.__dict__, d)

        r.update(1, 2, 3, 4)
        d["_Rectangle__x"] = 4
        self.assertEqual(r.__dict__, d)

        r.update(1, 2, 3, 4, 5)
        d["_Rectangle__y"] = 5
        self.assertEqual(r.__dict__, d)

    def test_26_update_args_bad(self):
        """Tests update() positional arg."""
        r = Rectangle(1, 2)
        d = r.__dict__.copy()

        r.update(1)
        d["id"] = 1
        self.assertEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r.update(1, "hello")
        s = "width must be an integer"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(1, -2)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(1, 2, -3)
        s = "height must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(1, 2, 3, -4)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(1, 2, 3, 4, -5)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

    def test_27_update_kwargs(self):
        """Tests update() keyword args."""
        r = Rectangle(1, 2)
        d = r.__dict__.copy()

        r.update(id=1)
        d["id"] = 1
        self.assertEqual(r.__dict__, d)

        r.update(width=2)
        d["_Rectangle__width"] = 2
        self.assertEqual(r.__dict__, d)

        r.update(height=3)
        d["_Rectangle__height"] = 3
        self.assertEqual(r.__dict__, d)

        r.update(x=4)
        d["_Rectangle__x"] = 4
        self.assertEqual(r.__dict__, d)

        r.update(y=5)
        d["_Rectangle__y"] = 5
        self.assertEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r.update(width="hi")
        s = "width must be an integer"
        self.assertEqual(str(e.exception), s)

# ---------- task 13 ----------------------------------

    def test_28_to_dictionary(self):
        """Tests to_dictionary() signature:"""
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r = Rectangle(1, 2)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

        r = Rectangle(1, 2, 3, 4, 5)
        d = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

        r.x = 10
        r.y = 20
        r.width = 30
        r.height = 40
        d = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(r.to_dictionary(), d)

if __name__ == "__main__":
    unittest.main()
