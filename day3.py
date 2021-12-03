#!/usr/bin/env python3
import sys

# read file
inputs = []
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        # split binary numbers into lists of bits
        inputs.append(list(map(lambda x: int(x), line.rstrip())))

gamma   = [0] * len(inputs[0])
epsilon = [0] * len(inputs[0])
bit     = [0] * len(inputs[0])
for number in inputs:
    for i in range(0, len(number)):
        bit[i] += number[i]

# most common bits
for i in range(0, len(bit)):
    if 2 * bit[i] >= len(inputs):
        gamma[i] = 1
    else:
        epsilon[i] = 1

def array_to_dec(arr):
    return int(''.join(map(lambda x: str(x), arr)), 2)

print ('Part 1  : ' + str(array_to_dec(gamma) * array_to_dec(epsilon)))

def compute_rating(numbers, keep, dont_keep):
    i = 0
    while i < len(numbers[0]) and len(numbers) > 1:
        bits_set = 0
        for number in numbers:
            bits_set += number[i]

        # most common bits
        if 2 * bits_set >= len(numbers):
            to_keep = keep
        else:
            to_keep = dont_keep

        if len(numbers) > 1:
            j = 0
            # remove numbers that don't share most common bit at this position
            while j < len(numbers):
                # remove this number, don't increment index
                # as it will now point to the next number
                if numbers[j][i] != to_keep:
                    del numbers[j]
                # don't remove, test next number
                else:
                    j += 1

        i += 1
    return numbers[0]

o2_numbers = inputs.copy()
co2_numbers = inputs.copy()

print ('Part 2  : ' + str(array_to_dec(compute_rating(o2_numbers, 1, 0)) * array_to_dec(compute_rating(co2_numbers, 0, 1))))
