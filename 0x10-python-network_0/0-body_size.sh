#!/bin/bash
#  takes in a URL and displays the size of the body of the response
curl -si $1 | grep Content-Length: | cut -d ":" -f2 | cut -d " " -f2
