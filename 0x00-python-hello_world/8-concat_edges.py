#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(" ")[5] + " " +  str.split(" ")[6] + " " + str.split(" ")[12] + " " + str.split(" ")[-16]
print(str)
