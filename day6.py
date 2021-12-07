#!/usr/bin/env python3
import sys

timers = [ 0 ] * 9;

# read file
with open(sys.argv[1], 'r') as f:
    fish = list(map(lambda x: int(x), f.readline().rstrip().split(',')))

# count how many fish have the same timers
for f in fish:
    timers[f] += 1

def evolve(timers):
    # just decrement timers
    # but 0 both count for a 6 and a new 8

    count8 = timers[0]
    for i in range(0, 8):
        timers[i] = timers[i+1]
        if i == 6:
            timers[i] += count8
    timers[8] = count8

def evolve7(timers):
    # after 7 iterations
    # 7 and 8 become 0 and 1, but no new fish
    count0 = timers[7]
    timers[7] = 0
    count1 = timers[8]
    timers[8] = 0

    # all other timers generate a fish with a timer of +2
    # and go back to their initial timer
    i = 6
    while i >= 0:
        timers[i+2] += timers[i]
        i -= 1
    timers[0] += count0
    timers[1] += count1

i=0
while i < 77:
    evolve7(timers)
    i += 7
while i < 80:
    evolve(timers)
    i += 1
print(f'Part 1 : : {sum(timers)}')

while i < 84:
    evolve(timers)
    i += 1
while i < 252:
    evolve7(timers)
    i += 7
while i < 256:
    evolve(timers)
    i += 1
print(f'Part 2 : : {sum(timers)}')
