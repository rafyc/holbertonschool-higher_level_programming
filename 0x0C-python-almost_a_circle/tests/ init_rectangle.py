#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle


class TestRect(unittest.TestCase):
    def test_rect_is_instance_base(self):
        r = Rectangle(10, 12, 5, 5, 0)
        self.assertIsInstance(r, Rectangle)


if __name__ == "__main__":
    unittest.main()
