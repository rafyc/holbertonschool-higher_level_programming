#!/usr/bin/env python3
"""Write a Python script that takes in a letter and sends a POST request
with the letter as a parameter.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'https://api.github.com/user'

    req = requests.get(url, auth=(argv[1], argv[2]))
    res = req.json()
    try:
        print(res['id'])
    except KeyError:
        print("None")
