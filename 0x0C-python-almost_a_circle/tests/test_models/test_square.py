#!/usr/bin/python3
"""
Unit test for the Square class
"""


import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquareSize(unittest.TestCase):
    """ tests for size setter/getter of square.py """

    def test_square_size1(self):
        """ test without args """
        with self.assertRaises(TypeError):
            Square.size()

    def test_square_0(self):
        """ test without args """
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_size2(self):
        """test getter"""
        my_square = Square(2)
        self.assertEqual(my_square.size, 2)

    def test_square_size3(self):
        """test setter"""
        my_square = Square(2)
        my_square.size = 7
        self.assertEqual(my_square.size, 7)

    def test_square_size4(self):
        """test setter with 0"""
        my_square = Square(2)
        with self.assertRaises(ValueError):
            my_square.size = 0

    def test_square_size5(self):
        """test setter with negative value"""
        my_square = Square(2)
        with self.assertRaises(ValueError):
            my_square.size = -5

    def test_square_size6(self):
        """test setter with wrong type: float"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = 4.5

    def test_square_size7(self):
        """test setter with wrong type: string"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = "School"

    def test_square_size8(self):
        """test setter with wrong type: list"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = [4]

    def test_square_size9(self):
        """test setter with wrong type: tuple"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = (4, )

    def test_square_size10(self):
        """test setter with wrong type: dictionary"""
        my_square = Square(2)
        with self.assertRaises(TypeError):
            my_square.size = {4}


class TestSquareUpdate_args(unittest.TestCase):
    """Unittest for update(*args) method of Square instance"""

    def test_args_not_specified(self):
        """Test with no specified parameters"""
        s = Square(4, 2, 3, 1)
        s.update()
        self.assertEqual("[Square] (1) 2/3 - 4", str(s))

    def test_args_one_parameter(self):
        """Test with one parameter"""
        s = Square(4, 2, 3, 1)
        s.update(5)
        self.assertEqual("[Square] (5) 2/3 - 4", str(s))

    def test_args_two_parameters(self):
        """Test with two parameters"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6)
        self.assertEqual("[Square] (5) 2/3 - 6", str(s))

    def test_args_three_parameters(self):
        """Test with three parameters"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6, 7)
        self.assertEqual("[Square] (5) 7/3 - 6", str(s))

    def test_args_four_parameters(self):
        """Test with four parameters"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6, 7, 8)
        self.assertEqual("[Square] (5) 7/8 - 6", str(s))

    def test_args_multiple_call(self):
        """Test with multiple use of update() method"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6, 7, 8)
        s.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def test_args_with_none(self):
        """Test with None"""
        s = Square(4, 2, 3, 1)
        s.update(None)
        self.assertEqual("[Square] (None) 2/3 - 4", str(s))

    def test_args_size_is_none(self):
        """Test with size is none"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, None)

    def test_args_x_is_none(self):
        """Test with x coordinate is none"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(2, 6, None)

    def test_args_y_is_none(self):
        """Test with y coordinate is none"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(2, 6, 1, None)

    def test_args_size_must_be_integer(self):
        """Test size parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(3600, "4")

    def test_args_size_zero(self):
        """Test size parameter with zero"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(3600, 0)

    def test_args_negative_size(self):
        """Test size with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(3600, -4)

    def test_args_x_must_be_integer(self):
        """Test x coordinate with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(3600, 6, "2")

    def test_args_negative_x(self):
        """Test x coordinate with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(3600, 6, -2)

    def test_args_y_must_be_integer(self):
        """Test y coordinate with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(3600, 6, 3, "4")

    def test_args_negative_y(self):
        """Test y coordinate with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(3600, 6, 3, -4)


class TestSquareUpdate_kwargs(unittest.TestCase):
    """Unittest for update(**kwargs) method of Square instance"""

    def test_kwargs_update_id(self):
        """Test update(id=value)"""
        s = Square(4, 2, 3, 1)
        s.update(id=3600)
        self.assertEqual("[Square] (3600) 2/3 - 4", str(s))

    def test_kwargs_update_size(self):
        """Test update(size=value)"""
        s = Square(4, 2, 3, 1)
        s.update(size=8)
        self.assertEqual("[Square] (1) 2/3 - 8", str(s))

    def test_kwargs_update_x(self):
        """Test update(x=value)"""
        s = Square(4, 2, 3, 1)
        s.update(x=6)
        self.assertEqual("[Square] (1) 6/3 - 4", str(s))

    def test_kwargs_update_y(self):
        """Test update(y=value)"""
        s = Square(4, 2, 3, 1)
        s.update(y=8)
        self.assertEqual("[Square] (1) 2/8 - 4", str(s))

    def test_kwargs_update_all(self):
        """Test update(id, size, x, y)"""
        s = Square(4, 2, 3, 1)
        s.update(y=8, size=16, id=3600, x=4)
        self.assertEqual("[Square] (3600) 4/8 - 16", str(s))

    def test_kwargs_multiple_call(self):
        """Test with multiple update call"""
        s = Square(4, 2, 3, 1)
        s.update(y=8, size=16, id=3600, x=4)
        s.update(x=2, id=1, y=3, size=4)
        self.assertEqual("[Square] (1) 2/3 - 4", str(s))

    def test_kwargs_size_is_none(self):
        """Test update(size=None)"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size=None)

    def test_kwargs_x_is_none(self):
        """Test update(x=None)"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x=None)

    def test_kwargs_y_is_none(self):
        """Test update(y=None)"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y=None)

    def test_kwargs_size_must_be_integer(self):
        """Test size parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="4")

    def test_kwargs_size_zero(self):
        """Test size parameter with zero"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_kwargs_negative_size(self):
        """Test size parameter with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-4)

    def test_kwargs_x_must_be_integer(self):
        """Test x parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="2")

    def test_kwargs_negative_x(self):
        """Test x parameter with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-2)

    def test_kwargs_y_must_be_integer(self):
        """Test y parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="3")

    def test_kwargs_negative_y(self):
        """Test y parameter with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-3)


class TestSquare(unittest.TestCase):
    """
        tests for square to dictionary
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dict_square_ok(self):
        """
            tests for dictionary for a normal square
        """
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.to_dictionary(), {
                         'id': 1, 'x': 2, 'size': 10, 'y': 1})
        s1 = Square(10, 2, 1, 8)
        self.assertEqual(s1.to_dictionary(), {
                         'id': 8, 'x': 2, 'size': 10, 'y': 1})
        s5 = Square(3, 12)
        self.assertEqual(s5.to_dictionary(), {
                         'id': 2, 'x': 12, 'size': 3, 'y': 0})
        s6 = Square(3)
        self.assertEqual(s6.to_dictionary(), {
                         'id': 3, 'size': 3, 'x': 0, 'y': 0})

    def test_to_dict_square_value_error(self):
        """
            tests for value error of the square
        """
        with self.assertRaises(ValueError):
            s2 = Square(-2, 3, 12)
            s2.to_dictionary()
        with self.assertRaises(ValueError):
            s3 = Square(2, -3, 12)
            s3.to_dictionary()
        with self.assertRaises(ValueError):
            s4 = Square(2, 3, -12)
            s4.to_dictionary()

    def test_to_dict_square_type_error(self):
        """
            test for type error of the square
        """
        with self.assertRaises(TypeError):
            s7 = Square()
            s7.to_dictionary()
        with self.assertRaises(TypeError):
            s8 = Square(2.3, 3, 12)
            s8.to_dictionary()
        with self.assertRaises(TypeError):
            s9 = Square(2, 3.2, 12)
            s9.to_dictionary()
        with self.assertRaises(TypeError):
            s10 = Square(2, (3, 2, 3), 12)
            s10.to_dictionary()
        with self.assertRaises(TypeError):
            s11 = Square((2, 8, 9), 3, 12)
            s11.to_dictionary()
        with self.assertRaises(TypeError):
            s12 = Square(2, 3, (2, 8, 7))
            s12.to_dictionary()
        with self.assertRaises(TypeError):
            s13 = Square((), 3, 12)
            s13.to_dictionary()
        with self.assertRaises(TypeError):
            s14 = Square(2, (), 12)
            s14.to_dictionary()
        with self.assertRaises(TypeError):
            s15 = Square(2, 3, ())
            s15.to_dictionary()
        with self.assertRaises(TypeError):
            s16 = Square(float('inf'), 3, 12)
            s16.to_dictionary()
        with self.assertRaises(TypeError):
            s17 = Square(2, float('inf'), 12)
            s17.to_dictionary()
        with self.assertRaises(TypeError):
            s18 = Square(2, 12, float('inf'))
            s18.to_dictionary()


class Test_str_square(unittest.TestCase):
    """tests for the str of square"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str(self):
        """test normal use of str function"""
        s1 = Square(2, 1, 3, 6)
        self.assertEqual("[Square] (6) 1/3 - 2", str(s1))

    def test_str1(self):
        """test less informations"""
        s2 = Square(2, 1)
        self.assertEqual("[Square] (1) 1/0 - 2", str(s2))
        s3 = Square(3, 1, 6)
        self.assertEqual("[Square] (2) 1/6 - 3", str(s3))
        s4 = Square(3)
        self.assertEqual("[Square] (3) 0/0 - 3", str(s4))
        with self.assertRaises(TypeError):
            Square()

    def test_str2(self):
        """test wrong informations"""
        with self.assertRaises(ValueError):
            Square(-2)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(TypeError):
            Square(3.2)
        with self.assertRaises(TypeError):
            Square({1, 2})
        with self.assertRaises(TypeError):
            Square([1, 34])
        with self.assertRaises(TypeError):
            Square(float('inf'))


if __name__ == '__main__':
    unittest.main()
