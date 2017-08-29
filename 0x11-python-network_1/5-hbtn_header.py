#!/usr/bin/python3
# fetches url
import requests
import sys
if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print (req.headers["x-request-id"])
