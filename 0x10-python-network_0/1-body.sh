#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
# insists curl to follow the redirection
curl -L "$1"
