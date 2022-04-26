#!/usr/bin/python3


for letter in range(122, 96, -1):
    if letter % 2 == 0:
        print("{:c}".format(letter), end="")
    else:
        letter -= 32
        print("{:c}".format(letter), end="")
