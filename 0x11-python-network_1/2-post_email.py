#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

from urllib import request, parse
from urllib.request import urlopen
from sys import argv

if __name__ == '__main__':
    data = parse.urlencode({"email": argv[2]})
    data = data.encode('ascii')
    with urlopen(argv[1], data) as response:
        print(response.read().decode('utf-8'))
