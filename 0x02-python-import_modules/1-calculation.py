#!/usr/bin/python3


from calculator_1 import add, sub, mul, div
a = 10
b = 5

print("{} + {} = {}".format(a, b, add))
print("{} + {} = {}".format(a, b, sub))
print("{} + {} = {}".format(a, b, mul))
print("{} + {} = {}".format(a, b, div))

if __name__ == '__main__':
    add(a, b)
    sub(a, b)
    mul(a, b)
    div(a, b)
