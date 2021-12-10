#!/usr/bin/env python3
import sys

instr = []

# read file
with open(sys.argv[1], 'r') as f:
    for l in f.readlines():
        instr.append(l.rstrip())

closers = {'(': ')', '[': ']', '{': '}', '<': '>'}
openers = {')': '(', ']': '[', '}': '{', '>': '<'}

incorrect_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
incomplete_points = {')': 1, ']': 2, '}': 3, '>': 4}

def get_first_invalid(line):
    opened = []
    for c in list(line):
        if c in ['(', '[', '{', '<']:
            opened.append(c)
        else:
            if len(opened) and opened[len(opened)-1] == openers[c]:
                opened.pop()
            else:
                return {'char': c, 'opened': opened}
    return {'char': None, 'opened': opened}

#print(get_first_invalid('<[]{}{<>'))
total_points = 0
scores = []
for i in instr:
    inv = get_first_invalid(i)
    # first invalid char (part 1)
    if inv['char']:
        total_points += incorrect_points[inv['char']]
    # close all remaining tags and compute score (part 2)
    else:
        score = 0
        while len(inv['opened']):
            score *= 5
            score += incomplete_points[closers[inv['opened'].pop()]]
        scores.append(score)

print(f'Part 1 : {total_points}')

# for median value
scores.sort()

print(f'Part 2 : {scores[int(len(scores)/2)]}')
