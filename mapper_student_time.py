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
        try:
            author_id, hour = line[3], time.strptime(line[8][:-3], "%Y-%m-%d %H:%M:%S.%f").tm_hour
            writer.writerow([author_id, hour])
        except:
            continue
