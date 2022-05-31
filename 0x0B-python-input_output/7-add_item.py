#!/usr/bin/python3


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = "add_item.json"
try:
    mylist = load_from_json_file(file)
except Exception:
    mylist = []

for arguments in argv[1:]:
    mylist.append(arguments)
save_to_json_file(mylist, file)
