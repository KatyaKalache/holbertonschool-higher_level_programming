#!/bin/bash
# POST request to the passed URL, using variables dispalys response
curl -sd "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
