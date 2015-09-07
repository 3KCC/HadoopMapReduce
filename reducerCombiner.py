#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

def reducer():
    oldKey = None
    rowA = []
    rowB = []
    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        # YOUR CODE HERE
        if len(data_mapped) != 6 and len(data_mapped) != 10:
            continue

        thisKey, tp = data_mapped[0:2]
        if oldKey and oldKey != thisKey:
            print '{}\t{}'.format(*k) for k in (rowA + rowB)
            oldKey = thisKey
            rowA, rowB = [], []

        if tp == '"B"':
            rowB = [thisKey] + data_mapped[2:]
        else:
            rowA = data_mapped[2:]
        
        oldKey = thisKey

    if oldKey:
        print "{0}\t{1}".format(rowB, rowA)

reducer()
