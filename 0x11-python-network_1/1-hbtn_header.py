#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        req = response.info()
        print (req['x-request-id'])
