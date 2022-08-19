#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request
with the letter as a parameter.
"""

from urllib import request, parse
from urllib.request import urlopen
from sys import argv

if __name__ == '__main__':
    data = parse.urlencode({"email": argv[2]})
    data = data.encode('ascii')
    with urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
