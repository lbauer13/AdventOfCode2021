#!/usr/bin/env python3
import sys
from collections import Counter

template = ''
rules = dict()

# read file
found_empty = False
with open(sys.argv[1], 'r') as f:
    for l in f.readlines():
        if len(l) > 1:
            if found_empty:
                pieces = l.rstrip().split(' ')
                rules[pieces[0]] = pieces[2]
            else:
                template = l.rstrip()
        else:
            found_empty = True

def polymerize(string, rules, counts):
    new_string = ''
    new_counts = counts.copy()
    pieces = list(string)
    for i in range(len(pieces) - 1):
        new_string += pieces[i]
        key = pieces[i] + pieces[i+1]
        if key in rules.keys():
            # insert character
            new_string += rules[key]
            # but also update counts
            if rules[key] in new_counts.keys():
                new_counts[rules[key]] += 1
            else:
                new_counts[rules[key]] = 1
    new_string += pieces[len(pieces) - 1]
    return {'template': new_string, 'counts': new_counts}

def count_elements(string):
    counts = dict()
    for l in list(string):
        if l in counts.keys():
            counts[l] += 1
        else:
            counts[l] = 1
    return counts

# save template for part 2
template_save = template

counts = count_elements(template)

for i in range(10):
    new_t = polymerize(template, rules, counts)

    template = new_t['template']
    counts = new_t['counts']

# make a sorted array of values
a_counts = [ v for k, v in sorted(counts.items(), key=lambda item: item[1]) ]

print(f'Part 1 : {a_counts[len(a_counts)-1] - a_counts[0]}')

# 
# I was stuck on part 2, trying to find a pattern in polymerization,
# when I should have asked myself if I really needed to generate the polymer
# Found "inspiration" in https://www.reddit.com/r/adventofcode/comments/rfzq6f/2021_day_14_solutions/
#

# start over
template = template_save
pairs = [''.join(p) for p in zip(template, template[1:])]

# rules not only generate a character inserted, but actyally two other pairs
rules = { k: (k[0] + v, v + k[1]) for k,v in rules.items() }
counter = Counter(pairs)

for i in range(40):
    new_count = {key : 0 for key in rules.keys()}
    # for each pair, 2 other pairs are added
    for k,v in counter.items():
        new_count[rules[k][0]] += v
        new_count[rules[k][1]] += v
    counter = new_count

# then count characters as above
counts = { l: 0 for l in list(''.join(rules.keys())) }
for k,v in counter.items():
    counts[k[0]] += v
# don't forget last char
counts[template[len(template)-1]] += 1

# make sorted array
a_counts = [ v for k, v in sorted(counts.items(), key=lambda item: item[1]) ]

print(f'Part 2 : {a_counts[len(a_counts)-1] - a_counts[0]}')
