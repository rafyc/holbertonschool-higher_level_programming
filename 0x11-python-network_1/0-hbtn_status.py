#!/usr/bin/python3
"""THis module defines a script that fetches https://intranet.hbtn.io/status"""

from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode('utf_8')}")
