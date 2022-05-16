#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for (key, value) in sorted((a_dictionary).items()):
        print("{}: {}".format(key, value))
"""
 for k in sorted(a_dictionary):
        print("{}: {}".format(k, a_dictionary[k]))
        
 """
