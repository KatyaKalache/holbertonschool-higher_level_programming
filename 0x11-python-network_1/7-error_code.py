#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code < 399:
        print(req.text)
    else:
        print("Error code: ", req.status_code)
