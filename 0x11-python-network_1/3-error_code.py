#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)."""

if __name__ == '__main__':
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        print(response.read())
