#!/usr/bin/python3


from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import unittest


class TestRect(unittest.TestCase):
    def test_rect_is_instance_base(self):
        r = Rectangle(10, 12, 5, 5, 0)
        self.assertIsInstance(r, Rectangle)


if __name__ == "__main__":
    unittest.main()
