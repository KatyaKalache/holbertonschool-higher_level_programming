#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get('https://swapi.co/api/people/',
                       params={'search': argv[1]})
    json_format = req.json()
    results = json_format.get('results')
    count = json_format.get('count')
    print("Number of results:", count)
    for i in results:
        print(i.get('name'))
