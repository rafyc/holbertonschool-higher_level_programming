#!/usr/bin/python3


from os import remove


def delete_at(my_list=[], idx=0):
    if not 0 <= idx > len(my_list):
        del my_list[idx]
        return my_list
