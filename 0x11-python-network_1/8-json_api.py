#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request
with the letter as a parameter.
"""

from ast import arg


if __name__ == '__main__':
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"

    if argv[1]:
        myobj = {'q': argv[1]}
    else:
        myobj = {'q': ""}

    req = requests.post(url, data=myobj)

    print(req.text)
