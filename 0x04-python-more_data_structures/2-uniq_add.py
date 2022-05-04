#!/usr/bin/python3

def uniq_add(my_list=[]):

    somme = 0
    for num in set(my_list):
        somme += num

    return somme


"""
    somme = 0

    my_list = list(set(my_list))

    for num in my_list:
        somme += num

    return somme
 """
