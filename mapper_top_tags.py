#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv
import time

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\n')

for line in reader:
    if len(line) == 19:
        tagnames, node_type = line[2].strip().lower().split(), line[5].strip().lower()
        if node_type == 'question':
            writer.writerow(tagnames)
