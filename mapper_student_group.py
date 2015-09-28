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
        node_id, question_id, student_id = line[0], line[6], line[3]
        if question_id == "\N":
            writer.writerow([node_id, student_id])
        else:
            writer.writerow([question_id, student_id])
