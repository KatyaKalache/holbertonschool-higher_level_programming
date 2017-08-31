#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2]))
    json_format = req.json()
    print(json_format.get('id'))
