#!/usr/bin/python3


from sys import argv
result = 0


for number in range(1, len(argv)):
    result = result + int(argv[number])

print("{}".format(result))
