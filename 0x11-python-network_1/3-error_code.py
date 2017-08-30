#!/usr/bin/python3
#!/usr/bin/python3
import urllib.request
from sys import argv
from urllib.error import HTTPError

try:
    with urllib.request.urlopen(argv[1]) as response:
        req = response.read()
        print(req.decode("utf-8"))
except HTTPError as e:
        print('Error code:', e.code)
