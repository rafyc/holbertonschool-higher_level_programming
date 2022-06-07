#!/usr/bin/python3
"""
    Unittest for Base
"""

import unittest
import pycodestyle
from models import base
from models.rectangle import Rectangle
from models.square import Square
Base = base.Base


class TestBase_comments(unittest.TestCase):
    """
        test for comments for base rectangle and square files
    """

    def test_conformance_1(self):
        """
            Test that we conform to PEP-8 for Base
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)


class TestBase(unittest.TestCase):
    """
        test for Base
    """

    def setUp(self):
        """
            reset id
        """
        Base._Base__nb_objects = 0

    def test_creation_id(self):
        """
            test if value of id has the good assignment
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(-5)
        b6 = Base(6.3)
        b7 = Base()
        b8 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, -5)
        self.assertEqual(b6.id, 6.3)
        self.assertEqual(b7.id, 4)
        self.assertEqual(b8.id, 5)

    def test_id_int(self):
        """Test integer id"""
        b = Base(5)
        self.assertEqual(b.id, 5)
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base(-3)
        self.assertEqual(b.id, -3)

    def test_id_incrementation(self):
        """Test id incrementation"""
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(7)
        self.assertEqual(b.id, 7)
        b = Base(None)
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)

    def test_id_non_int(self):
        """Test non integer id"""
        b = Base("Holberton")
        self.assertEqual(b.id, "Holberton")
        b = Base('A')
        self.assertEqual(b.id, 'A')
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))
        b = Base({"id": 7, "name": "Betty"})
        self.assertEqual(b.id, {"id": 7, "name": "Betty"})
        b = Base(False)
        self.assertEqual(b.id, False)

    def test_id_error(self):
        """Test error"""
        with self.assertRaises(TypeError):
            b = Base(1, 2)
        with self.assertRaises(TypeError):
            b = Base(1, None)


class TestToJsonString(unittest.TestCase):
    """
    Unittest for to_json_string
    """

    def test_rectangle_to_str(self):
        """True if to_json_string return str type"""
        r1 = Rectangle(10, 7, 4, 6, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str, type(json_dictionary))

    def test_rectangle_instance(self):
        """Test rectangle instance with len()"""
        r1 = Rectangle(10, 7, 6, 4, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(len(json_dictionary) == 53)

    def test_more_rectangle_to_str(self):
        """True if to_json_string return str type"""
        r1 = Rectangle(10, 7, 4, 6, 1)
        r2 = Rectangle(7, 10, 6, 4, 1)
        dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertEqual(str, type(json_dictionary))

    def test_more_rectangle_instances(self):
        """Test rectangle instances with len()"""
        r1 = Rectangle(10, 7, 4, 6, 1)
        r2 = Rectangle(7, 10, 6, 4, 1)
        dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertTrue(len(json_dictionary) == 106)

    def test_square_to_str(self):
        """True if to_json_string return str type"""
        s1 = Square(10, 4, 6, 1)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string(dictionary)
        self.assertEqual(str, type(json_dictionary))

    def test_square_instance(self):
        """Test square instance with len()"""
        s1 = Square(10, 4, 6, 1)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string(dictionary)
        self.assertTrue(len(json_dictionary) == 37)

    def test_more_squares_to_str(self):
        """True if to_json_string return str type"""
        s1 = Square(10, 4, 6, 1)
        s2 = Square(7, 6, 4, 1)
        dictionaries = [s1.to_dictionary(), s2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertEqual(str, type(json_dictionary))

    def test_more_square_instances(self):
        """Test square instances with len()"""
        s1 = Square(10, 4, 6, 1)
        s2 = Square(7, 6, 4, 1)
        dictionaries = [s1.to_dictionary(), s2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertTrue(len(json_dictionary) == 77)

    def test_empty(self):
        """Test with empty value"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none(self):
        """Test with None"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_parameters(self):
        """Test if no parameter (list_dicitonaries)"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_parameters(self):
        """Test if more undefined parameters"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 3600)


if __name__ == '__main__':
    unittest.main()
