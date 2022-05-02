#!/usr/bin/python3


from os import remove


def delete_at(my_list=[], idx=0):
    for numbers in my_list:
        if numbers == idx:
            del my_list[idx]
    return my_list
