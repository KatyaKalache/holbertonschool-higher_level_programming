#!/usr/bin/python3
# fetches url
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get("x-request-id"))
