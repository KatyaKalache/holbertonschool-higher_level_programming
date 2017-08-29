#!/usr/bin/python3
# retrieving request id
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    req = response.info()
print (req['x-request-id'])
