#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST request
with the letter as a parameter.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"

    if len(argv) == 1:
        myobj = {'q': ""}
    else:
        myobj = {'q': argv[1]}

    req = requests.post(url, data=myobj)

    try:
        my_dict = req.json()
        if len(my_dict) == 0:
            print("No result")
        else:
            print("{} {}".format(my_dict['id'], my_dict['name']))
    except ValueError:
        print('Not a valid JSON')


