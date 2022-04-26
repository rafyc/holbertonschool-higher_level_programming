#!/usr/bin/python3

i = 122
temp = 32
while i >= 65:
    print("{:c}".format(i), end="")
    if i == 65:
        break
    i -= 1
    i -= temp
    temp *= -1
