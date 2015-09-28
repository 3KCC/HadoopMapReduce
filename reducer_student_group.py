#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

oldKey = None
students = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisStudent = data_mapped

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}".format(oldKey, students)
        oldKey = thisKey
        students = []

    oldKey = thisKey
    students.append(thisStudent)

if oldKey:
    print "{0}\t{1}".format(oldKey, students)
