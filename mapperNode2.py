#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import re
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')
delimiters = "[\.,!\?:;\"()<>\[\]#\$-=\/\s]"

for line in reader:
	if len(line) == 19:
		node_id, body = line[0], line[4]
		#split body by delimiters
		keywords = filter(None ,re.split(delimiters, body.strip()) )
		# #remove duplicates
		# #keywords = list(set(keywords))
		for key in keywords:
			writer.writerow([key.lower(), node_id])
