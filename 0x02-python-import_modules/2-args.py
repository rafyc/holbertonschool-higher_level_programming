#!/usr/bin/python3


from sys import argv
i = 1

if len(argv) == 1:
    print("0 argument.")
else:
    print("{} arguments".format(len(argv) - 1))

for argument in range(1, len(argv)):
    print("{}: {}".format(i, argv[i]))
    i += 1
