#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary

""" 
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, none)
    return a_dictionary

"""
