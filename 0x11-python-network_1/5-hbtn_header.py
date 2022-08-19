#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.get(argv[1])
    header = req.headers.get('X-Request-Id')
    print(header)
