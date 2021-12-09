#!/usr/bin/env python3
import sys

input  = []
input2 = []

# read file
with open(sys.argv[1], 'r') as f:
    for l in f.readlines():
        parts = l.rstrip().split('|')
        patterns = [ p for p in parts[0].split(' ') if p != '' ]
        output = [ p for p in parts[1].split(' ') if p != '' ]
        input.append({'patterns': patterns, 'output': output})
        input2.append({'patterns': patterns.copy(), 'output': output.copy()})

def get_easy_digits(display, where):
    count = 0
    digits = [ [] ] * 10;
    i = 0
    while i < len(display[where]):
        p = ordered(display[where][i])

        found = False
        if len(p) == 2:
            digits[1] = ''.join(p)
            found = True
        if len(p) == 4:
            digits[4] = ''.join(p)
            found = True
        if len(p) == 3:
            digits[7] = ''.join(p)
            found = True
        if len(p) == 7:
            digits[8] = ''.join(p)
            found = True
        if found:
            count += 1
            del(display[where][i])
        else:
            i += 1
    return {'count': count, 'digits': digits}

def includes(including, included):
    intersection = [ c for c in list(including) if c in list(included) ]
    intersection.sort()
    return (intersection == ordered(included))

def ordered(string):
    parts = list(string)
    parts.sort()
    return parts

count_easy = 0
for d in input:
    digits = get_easy_digits(d, 'output')
    count_easy += digits['count']

print ('Day 1 : ' + str(count_easy))

part2 = 0
for d in input2:
    # collect easy digits : 1, 4, 7 and 8
    digits = get_easy_digits(d, 'patterns')['digits']

    # next, check all 6-segment digits
    # and check which known segment they include
    i = 0
    while i < len(d['patterns']):
        p = d['patterns'][i]
        o = ''.join(ordered(p))
        if len(p) == 6:
            if includes(p, digits[4]):
                digits[9] = o
            elif includes(p, digits[1]):
                digits[0] = o
            else:
                digits[6] = o
            del(d['patterns'][i])
        else:
            i += 1
    # same with 5-segmetns digits
    i = 0
    while i < len(d['patterns']):
        p = d['patterns'][i]
        o = ''.join(ordered(p))
        found = False
        if len(p) == 5:
            if includes(p, digits[1]):
                digits[3] = o
                found = True
            elif includes(digits[9], p):
                digits[5] = o
                found = True
        if found:
            del(d['patterns'][i])
        else:
            i += 1

    # last digit is 2
    digits[2] = ''.join(ordered(d['patterns'][0]))

    # now we have all digits sorted, just decode output in decimal
    output = 0
    for digit in d['output']:
        o = ''.join(ordered(digit))
        x = digits.index(o)
        output *= 10
        output += x

    # general sum
    part2 += output

print(f'Part 2 : {part2}')
