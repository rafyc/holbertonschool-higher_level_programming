#!/usr/bin/python3


from re import A


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
