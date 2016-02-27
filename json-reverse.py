#!/usr/bin/python

import json
from sys import argv

script, filename = argv

file = open("results.txt" , "a")

json_data = json.loads(open(filename , "r").read())
json_length = len(json_data) + 1

for i in range(1, json_length):
        name = json_data["key%d" % (i)]["name"]
        rev_name = name[::-1]
        file.write(rev_name)
        file.write("\n")

file.close()