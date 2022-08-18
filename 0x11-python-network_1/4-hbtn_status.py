#!/usr/bin/python3
"""THis module defines a script that fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    response = requests.get('https://intranet.hbtn.io/status')
    req = response.text
    print("Body response:")
    print(f"\t- type: {type(req)}")
    print(f"\t- content: {req}")
