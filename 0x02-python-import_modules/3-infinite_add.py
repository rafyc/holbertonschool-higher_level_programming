#!/usr/bin/python3


from sys import argv

if __name__ == "__main__":

    result = 0

    for number in range(1, len(argv)):
        result = result + int(argv[number])

    print("{}".format(result))
