#!/usr/bin/env python3
import sys

# read file
inputs = []
with open(sys.argv[1], 'r') as f:
    inputs = list(map(lambda l: l.rstrip(), f.readlines()))

def move_all(aiming):
    h_pos = 0
    d_pos = 0
    aim   = 0
    for i in inputs:
        arr = i.split()
        direction = arr[0]
        count = int(arr[1])
        if direction == 'forward':
            h_pos += count
            # no need to test, if not aiming, aim = 0
            d_pos += count * aim
        if direction == 'up':
            if aiming:
                aim -= count
            else:
                d_pos -= count
        if direction == 'down':
            if aiming:
                aim +=count
            else:
                d_pos += count
    return h_pos * d_pos

print ('Part 1 : ' + str(move_all(False)))
print ('Part 2 : ' + str(move_all(True)))
