#!/bin/bash
#  takes in a URL and displays the size of the body of the response
curl -si 0.0.0:5000 | grep Content-Length: | cut -d ":" -f2
