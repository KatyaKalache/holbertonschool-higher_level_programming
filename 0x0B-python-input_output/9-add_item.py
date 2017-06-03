#!/usr/bin/python3
import json
import sys
import os.path


save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file
my_list = []

if not os.path.exists("./add_item.json"):
    save(my_list, "add_item.json")
my_list = load("add_item.json")

for i in sys.argv[1:]:
    my_list.append(i)
save(my_list, "add_item.json")
