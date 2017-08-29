#!/usr/bin/python3
# fetches url
import requests
import json
req = requests.get('https://intranet.hbtn.io/status')
print ("Body response:")
print ("    - type: ", end="")
print (type(str(req)))
print ("    - content: ", end="")
print (req.text)
