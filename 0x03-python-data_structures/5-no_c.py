#!/usr/bin/python3


def no_c(my_string):
    newstring = ""
    if my_string:
        for letter in my_string:
            if letter != 'c' and letter != 'C':
                newstring += letter
        return newstring
