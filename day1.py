#!/usr/bin/env python3
import sys

# read file, convert strings to integers
inputs = []
with open(sys.argv[1], 'r') as f:
    inputs = list(map(lambda x: int(x), f.readlines()))

# count number of increases in a list
def count_increases(measures):
    last = None
    count_positive = 0
    for i in measures:
        if (last and i > last):
            count_positive += 1
        last = i
    return count_positive

print('Part 1 : %d' % count_increases(inputs))

# compute 3-measurements sliding window
three = []
for i in range(0, len(inputs)-2):
    s = inputs[i] + inputs[i+1] + inputs[i+2]
    three.append(s)

print('Part 2 : %d' % count_increases(three))
