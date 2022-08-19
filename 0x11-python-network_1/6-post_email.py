#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    myobj = {'email': argv[2]}

    x = requests.post(url, data=myobj)

    print(x.text)
