#!/usr/bin/python3
import urllib.request
from sys import argv

if __name__ == "__main__":
    email = {}
    email["email"] = argv[2]
    value = urllib.parse.urlencode(email)
    with urllib.request.urlopen(argv[1], value) as response:
        req = response.read()
        print(req.decode("utf-8"))
