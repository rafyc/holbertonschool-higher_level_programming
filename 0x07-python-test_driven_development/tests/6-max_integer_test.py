#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_negatif(self):
        list = [5, 33]
        self.assertEqual(max_integer(list), 33)

    def test_string(self):
        list = ["raaaaa", "raf"]
        self.assertEqual(max_integer(list), "raf")

    def test_nothing(self):
        list = []
        self.assertEqual(max_integer(list), None)

    def test_neg(self):
        list = [-3, -10]
        self.assertEqual(max_integer(list), -3)

    def test_float(self):
        list = [3.33, 4.33]
        self.assertEqual(max_integer(list), 4.33)

    def test_solo(self):
        list = [33]
        self.assertEqual(max_integer(list), 33)


if __name__ == '__main__':
    unittest.main()
