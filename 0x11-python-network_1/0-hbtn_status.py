#!/usr/bin/python3
# fetches the url
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print ("Body response:")
        print ("    - type: ", end="")
        print (type(html))
        print ("    - content: ", end="")
        print (html)
        print ("    - utf8 content: ", end="")
        print (html.decode("utf-8"))
