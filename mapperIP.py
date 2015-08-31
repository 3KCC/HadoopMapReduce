#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

for line in sys.stdin:
    data = line.strip().split("\"")
    if len(data) == 3:
    	request = data[1]
    	part1 = filter(None, re.split('\\[|\\]', data[0].strip()))
    	if len(part1) == 2:
    		part1a = part1[0].strip().split(" ")
    		time = part1[1]
    		if len(part1a) == 3:
    			ip, clientId, username = part1a
    			print "{0}".format(ip)
