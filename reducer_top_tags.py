#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

oldKey = None
minimum = None
top10 = {}
count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
        if len(top10) < 10:
            top10[oldKey] = count
        else:
            if not minimum:
                minimum = min(top10.values())
                key_min = min(top10, key=top10.get)
            if count > minimum:
                del top10[key_min]
                top10[oldKey] = count
                minimum = min(top10.values())
                key_min = min(top10, key=top10.get)
        oldKey = thisKey
        count = 0

    oldKey = thisKey
    count += 1

if oldKey:
    if len(top10) < 10:
            top10[oldKey] = count
    else:
        if not minimum:
            minimum = min(top10.values())
            key_min = min(top10, key=top10.get)
        if count > minimum:
            del top10[key_min]
            top10[oldKey] = count
    for key in sorted(top10, key=top10.get, reverse=True):
        print "{0}\t{1}".format(key, top10[key])
