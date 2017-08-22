#!/bin/bash
#  takes in a URL and displays the size of the body of the response
curl -s -w \%{size_header} -o /dev/null $1
