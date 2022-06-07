#!/usr/bin/python3
"""
Unit test for the Rectangle class
"""


import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
from unittest.mock import patch
import io


class TestRectangle_setter_getter(unittest.TestCase):
    """test getter setter of the rectangle height and width"""

    def test_height_getter(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(3, rect.height)

    def test_height_setter(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.height = 12
        self.assertEqual(12, rect.height)

    def test_height_setter_0(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_height_setter_negative(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            rect.height = -12

    def test_height_setter_float(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = 1.2

    def test_height_setter_string(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = "ok"

    def test_height_setter_list(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = [12]

    def test_height_setter_tuple(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = (1, 2)

    def test_height_setter_dict(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.height = {12}

    def test_width_getter(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(2, rect.width)

    def test_width_setter(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.width = 12
        self.assertEqual(12, rect.width)

    def test_width_setter_0(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_width_setter_negative(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            rect.width = -12

    def test_width_setter_float(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.width = 1.2

    def test_width_setter_string(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.width = "ok"

    def test_width_setter_list(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.width = [12]

    def test_width_setter_tuple(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.width = (1, 2)

    def test_width_setter_dict(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.width = {12}


class TestRectangle(unittest.TestCase):
    """class testing the to_dictionary method and __str__ of Rectangle"""

    def test_to_dictionary(self):
        """test the to_dictionary method"""
        Base._Base__nb_objects = 0
        a = Rectangle(6, 2)
        output = {'id': 1, 'width': 6, 'height': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(1, 3, 5)
        output = {'id': 2, 'width': 1, 'height': 3, 'x': 5, 'y': 0}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(4, 4, 1, 6)
        output = {'id': 3, 'width': 4, 'height': 4, 'x': 1, 'y': 6}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(2, 7, 4, 2, 18)
        output = {'id': 18, 'width': 2, 'height': 7, 'x': 4, 'y': 2}
        self.assertDictEqual(a.to_dictionary(), output)

    def test_str(self):
        """test the output of the instance when printed"""
        Base._Base__nb_objects = 0
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print(Rectangle(4, 8))
        assert fake_stdout.getvalue() == '[Rectangle] (1) 0/0 - 4/8\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print(Rectangle(1, 3, 5, 7, 12))
        assert fake_stdout.getvalue() == '[Rectangle] (12) 5/7 - 1/3\n'

    def test_exception(self):
        """test with exception"""
        a = Rectangle(1, 2, 3, 4, 6)
        self.assertRaises(TypeError, a.to_dictionary, 0)
        a = Rectangle(1, 2)
        self.assertRaises(TypeError, a.to_dictionary, None)


class TestArea(unittest.TestCase):
    """ test area for class rectangle.py """

    def test_area_rectangle1(self):
        """ test with 2 integers """
        a = Rectangle(3, 5)
        self.assertEqual(a.area(), 15)

    def test_area_rectangle2(self):
        """ test with float for width and int for height"""
        with self.assertRaises(TypeError):
            a = Rectangle(0.3, 5)
            a.area()

    def test_area_rectangle3(self):
        """ test with int for width and float for heigt """
        with self.assertRaises(TypeError):
            a = Rectangle(3, 0.5)
            a.area()

    def test_area_rectangle4(self):
        """ test with 0 for width and int for height """
        with self.assertRaises(ValueError):
            a = Rectangle(0, 5)
            a.area()

    def test_area_rectangle5(self):
        """ test with int for widht and 0 for height """
        with self.assertRaises(ValueError):
            a = Rectangle(3, 0)
            a.area()

    def test_area_rectangle6(self):
        """ test for negative for width and int for height """
        with self.assertRaises(ValueError):
            a = Rectangle(-3, 5)
            a.area()

    def test_area_rectangle7(self):
        """ test with negative for width & height """
        with self.assertRaises(ValueError):
            a = Rectangle(-3, -5)
            a.area()

    def test_area_rectangle8(self):
        """ test with 1 arg """
        with self.assertRaises(TypeError):
            a = Rectangle(3)
            a.area()

    def test_area_rectangle9(self):
        """ test without arg """
        with self.assertRaises(TypeError):
            a = Rectangle()
            a.area()

    def test_area_rectangle10(self):
        """ test with arg None """
        with self.assertRaises(TypeError):
            a = Rectangle(None)
            a.area()

    def test_area_rectangle11(self):
        """ test with function for width and int for height """
        with self.assertRaises(UnboundLocalError):
            a = Rectangle(a.area(), 6)
            a.area()

    def test_area_rectangle12(self):
        """ test with strings """
        with self.assertRaises(TypeError):
            a = Rectangle("Hello!", "World")
            a.area()

    def test_area_rectangle13(self):
        """ test with tuples """
        with self.assertRaises(TypeError):
            a = Rectangle((1, 2, 3), (1, 2, 3))
            a.area()

    def test_area_rectangle14(self):
        """ test with lists """
        with self.assertRaises(TypeError):
            a = Rectangle([1, 2, 3], [1, 2, 3])
            a.area()

    def test_area_rectangle15(self):
        """ test with dictionaries """
        with self.assertRaises(TypeError):
            a = Rectangle({1, 2, 3}, {1, 2, 3})
            a.area()

    def test_area_rectangle16(self):
        """ test with float("inf") for width """
        with self.assertRaises(TypeError):
            a = Rectangle(float("inf"), 3)
            a.area()

    def test_area_rectangle17(self):
        """ test float("Nan") for width """
        with self.assertRaises(TypeError):
            a = Rectangle(float("NaN"), 5)
            a.area()

    def test_area_rectangle18(self):
        """ test with None for args """
        with self.assertRaises(TypeError):
            a = Rectangle(None, None)
            a.area()

    def test_area_rectangle19(self):
        """ test with string for width int for height """
        with self.assertRaises(TypeError):
            a = Rectangle("Hello!", 5)
            a.area()

    def test_area_rectangle20(self):
        """ test with int for width string for height """
        with self.assertRaises(TypeError):
            a = Rectangle(3, "World")
            a.area()

    def test_area_rectangle21(self):
        """ test with 1 string """
        with self.assertRaises(TypeError):
            a = Rectangle("Hello!")
            a.area()

    def test_area_rectangle22(self):
        """ test with 1 string """
        with self.assertRaises(TypeError):
            a = Rectangle.area()


class TestUpdate(unittest.TestCase):
    """ test update for class rectangle.py """

    def test_update1(self):
        """ test without args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update()
        self.assertEqual('[Rectangle] (10) 10/10 - 10/10', str(a))

    def test_update2(self):
        """ test with 1 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(a))

    def test_update3(self):
        """ test with 2 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 1)
        self.assertEqual("[Rectangle] (89) 10/10 - 1/10", str(a))

    def test_update4(self):
        """ test with 3 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 1, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 1/2", str(a))

    def test_update6(self):
        """ test with 5 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 1, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(a))

    def test_update7(self):
        """ test with id None """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(None)
        self.assertEqual("[Rectangle] (None) 10/10 - 10/10", str(a))

    def test_update8(self):
        """ test with id None and args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(None, 1, 2, 3)
        self.assertEqual("[Rectangle] (None) 3/10 - 1/2", str(a))

    def test_update9(self):
        """ test with twice update """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 1, 2, 3, 4)
        a.update(5, 6, 7, 8, 9)
        self.assertEqual("[Rectangle] (5) 8/9 - 6/7", str(a))

    def test_update10(self):
        """ test with strings for width """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a.update(89, "Hello!")

    def test_update11(self):
        """ test with 0 for width"""
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a.update(89, 0)

    def test_update12(self):
        """ test with negative for width """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a.update(89, -1)

    def test_update13(self):
        """ test update with string for height """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a.update(89, 1, "Hello!")

    def test_update14(self):
        """ test with 0 for height """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            a.update(89, 1, 0)

    def test_update15(self):
        """ test with negative for height """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            a.update(89, 1, -2)

    def test_update16(self):
        """ test with string for x """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a.update(89, 1, 2, "Hello!")

    def test_update17(self):
        """ test with negative for y """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            a.update(89, 1, 2, 3, -4)

    def test_update18(self):
        """ test with strings for width and height """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a.update(89, "Hello!", "World")

    def test_update19(self):
        """ test with strings for width and x """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a.update(89, "Hello!", 1, "World")

    def test_update20(self):
        """ test with strings for width and y """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a.update(89, "Hello!", 1, 2, "World")

    def test_update21(self):
        """ test with strings for x and y """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a.update(89, 1, "Hello!", "World")

    def test_update22(self):
        """ test with strings height and y """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "Hello!", 1, "World")

    def test_update23(self):
        """ test with strings for x and y """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "Hello!", "World")

    def test_update24(self):
        """ test with id 0 """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(0)
        correct = f"[Rectangle] (0) 10/10 - 10/10"
        self.assertEqual(correct, str(a))

    def test_update25(self):
        """ test with id None """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(-1)
        correct = f"[Rectangle] (-1) 10/10 - 10/10"
        self.assertEqual(correct, str(a))

    def test_update27(self):
        """ test with args width is negative"""
        a = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a.update(width=-1, x=2, id=98)

    def test_update28(self):
        """ test with 3 attributes """
        a = Rectangle(10, 10, 10)
        a.update(98)
        self.assertEqual('[Rectangle] (98) 10/0 - 10/10', str(a))

    def test_update29(self):
        """ test with 3 attributes and without args """
        a = Rectangle(10, 10)
        a.update(98)
        self.assertEqual('[Rectangle] (98) 0/0 - 10/10', str(a))

    def test_update30(self):
        """ test with 3 attributes and without args """
        a = Rectangle(10, 10, 10, 10)
        a.update(width=1, x=2, id=98)
        self.assertEqual('[Rectangle] (98) 2/10 - 1/10', str(a))

    def test_update31(self):
        """ test with args x is string """
        a = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a.update(width=1, x="Hello!", id=98)

    def test_update32(self):
        """ test with args x is string """
        a = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a.update(width=0, x=2, id=98)


class TestRectangle(unittest.TestCase):
    """
        tests for Rectangle
    """

    def test_weight_is_integer(self):
        """
            test weight is int
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r3.width, 10)
        with self.assertRaises(ValueError):
            Rectangle(-2, 4)
        with self.assertRaises(TypeError):
            Rectangle(2.3, 5)
        with self.assertRaises(TypeError):
            Rectangle(None, 2)
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 2)
        with self.assertRaises(TypeError):
            Rectangle("abc", 2)
        with self.assertRaises(TypeError):
            Rectangle({1, 2}, 2)

    def test_height_is_integer(self):
        """
            test height is int
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r3.height, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, -4)
        with self.assertRaises(TypeError):
            Rectangle(2, 5.3)
        with self.assertRaises(TypeError):
            Rectangle(2, None)
        with self.assertRaises(TypeError):
            Rectangle(2, float('inf'))
        with self.assertRaises(TypeError):
            Rectangle(10, "hello", 2, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, {1, 2}, 0, 0, 12)

    def test_x_is_integer(self):
        """
            test x is int
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2, 3, 0, 12)

        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3.5, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, None, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, float('inf'), 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, (1, 2), 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "hello", 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {1, 2}, 0, 12)

    def test_y_is_integer(self):
        """
            test y is int
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2, 3, 2, 12)

        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -2, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, 2.6, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, None, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, float('inf'), 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, (1, 2, 3), 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "hello", 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, {1, 2}, 12)

    def test_area(self):
        """
            test the calculation of the area
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 3, 3, 2, 12)

        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 30)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -2, 0, 0, 12)
            r3.area()
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, 3, 3, 2, 12)
            r4.area()


class TestRectangle(unittest.TestCase):
    """
        tests for Rectangle
    """

    def test_rectangle_is_instance_of_base(self):
        """Test if the Rect is an instance of base
        """
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsInstance(r1, Base)

    def test_value_is_int(self):
        """Test if the value for init is an int
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("f", "f", "f", "f", "f")

    def test_value_is_negativ(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, -2, -2, -0, -12)

    def test_value_is_width_heigt_not_neg(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 0, -2, -0, -12)

    def test_value_is_x_y_not_neg(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 10, -1, -1, 12)

    def test_value_is_not_tuple(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle((1, -10), -2, -2, -0, -12)

    def test_value_is_not_list(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle([1, -10], -2, -2, -0, -12)

    def test_value_is_not_dict(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle({'lolo': -10}, -2, -2, -0, -12)

    def test_value_is_not_empty(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_display_None(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None, None, None)


class TestRectangle_setter_getter_x_y(unittest.TestCase):
    """test getter setter of the rectangle x and y"""

    def test_x_getter(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(4, rect.x)

    def test_x_setter(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.x = 12
        self.assertEqual(12, rect.x)

    def test_x_setter_negative(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            rect.x = -12

    def test_x_setter_0(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.x = 0
        self.assertEqual(0, rect.x)

    def test_x_setter_float(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.x = 1.2

    def test_x_setter_string(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.x = "ok"

    def test_x_setter_list(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.x = [12]

    def test_x_setter_tuple(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.x = (1, 2)

    def test_x_setter_dict(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.x = {12}

    def test_y_getter(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(5, rect.y)

    def test_y_setter(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.y = 12
        self.assertEqual(12, rect.y)

    def test_y_setter_negative(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(ValueError):
            rect.y = -12

    def test_y_setter_0(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        rect.y = 0
        self.assertEqual(0, rect.y)

    def test_y_setter_float(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.y = 1.2

    def test_y_setter_string(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.y = "ok"

    def test_y_setter_list(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.y = [12]

    def test_y_setter_tuple(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.y = (1, 2)

    def test_y_setter_dict(self):
        rect = Rectangle(2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            rect.y = {12}


if __name__ == '__main__':
    unittest.main()
