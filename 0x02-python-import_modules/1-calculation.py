#!/usr/bin/python3


import calculator_1

a = 10
b = 5

add = calculator_1.add(a, b)
sub = calculator_1.sub(a, b)
mul = calculator_1.mul(a, b)
div = calculator_1.div(a, b)

print("{} + {} = {}".format(a, b, add))
print("{} + {} = {}".format(a, b, sub))
print("{} + {} = {}".format(a, b, mul))
print("{} + {} = {}".format(a, b, div))
