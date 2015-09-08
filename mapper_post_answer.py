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
writer = csv.writer(sys.stdout, delimiter='\t')

for line in reader:
    if len(line) == 19:
        node_id, body, node_type, parent_id = line[0], line[4].strip(), line[5].strip().lower(), line[6]
        if node_type == 'question':
            writer.writerow([node_id, node_type, len(body)])
        if node_type == 'answer':
            writer.writerow([parent_id, node_type, len(body)])
