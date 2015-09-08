#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

oldKey = None
aLens = []
avgALen = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue

    thisKey, thistype, thisLen = data_mapped

    if oldKey and oldKey != thisKey:
        if aLens:
            avgALen = sum(aLens)/len(aLens)
        print "{0}\t{1}\t{2}".format(oldKey, qLen, avgALen)
        oldKey = thisKey
        aLens = []
        avgALen = 0

    oldKey = thisKey
    if thistype == 'answer':
        aLens.append(float(thisLen))
    if thistype == 'question':
        qLen = thisLen

if oldKey:
    if aLens:
        avgALen = sum(aLens)/len(aLens)
    print "{0}\t{1}\t{2}".format(oldKey, qLen, avgALen)
