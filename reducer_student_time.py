#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

oldKey = None
hourDict = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisHour = data_mapped

    if oldKey and oldKey != thisKey:
        highest = max(hourDict.values())
        for k,v in hourDict.items():
            if v == highest:
                print "{0}\t{1}".format(oldKey, k)
        oldKey = thisKey
        hourDict = {}

    oldKey = thisKey
    if thisHour in hourDict:
        hourDict[thisHour] += 1
    else:
        hourDict[thisHour] = 1

if oldKey:
    highest = max(hourDict.values())
    for k,v in hourDict.items():
        if v == highest:
            print "{0}\t{1}".format(oldKey, k)
