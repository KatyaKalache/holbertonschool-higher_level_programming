#!/usr/bin/python3
# post an email
import requests
import sys

if __name__ == "__main__":
    email = {}
    email["email"] = sys.argv[2]
    req = requests.post(sys.argv[1], email)
    print(req.content.decode("utf-8"))
