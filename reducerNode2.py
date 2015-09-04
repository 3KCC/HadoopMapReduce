#!/usr/bin/python

import sys

occurencesTotal = 0
oldKey = None
nodes = []

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNode = data_mapped
    if thisKey.strip() == 'fantastically':
        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, sorted(nodes))
            oldKey = thisKey;
            try:
                nodes = [int(thisNode)]
            except:
                nodes = []
        try:
            if int(thisNode) not in nodes:
                nodes.append(int(thisNode))
        except:
            continue

        oldKey = thisKey

if oldKey != None:
    print "{0}\t{1}".format(oldKey, sorted(nodes))
