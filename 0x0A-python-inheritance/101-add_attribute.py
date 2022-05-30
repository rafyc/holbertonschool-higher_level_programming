#!/usr/bin/python3


def add_attribute(a, key, value):
    if hasattr(a, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(a, key, value)
