#!/usr/bin/env python3
import sys

# read file
with open(sys.argv[1], 'r') as f:
    positions = list(map(lambda x: int(x), f.readline().rstrip().split(',')))

# could use statistics package, but then where's the fun ?
def median(values):
    values.sort()
    return values[int(len(values) / 2)]

median_pos = median(positions)
avg_pos = int(sum(positions) / len(positions))

#print(f'average {avg_pos}, median {median_pos}')

# compute fuel consumptions to align all crabs
# with constant rate (part 1), or increasing rate (part 2)
def sum_fuel(positions, target, constant):
    fuel = 0
    for p in positions:
        offset = abs(p - target)
        if constant:
            fuel += offset
        else:
            # 1 + 2 + ... + n = (n * (n +1 )) / 2
            fuel += (offset * (offset + 1)) / 2
    return fuel

print('Day 1 : ', sum_fuel(positions, median_pos, True))

# best position is surely between average and median values
#fuel_values = []
#for pos in range(min([median_pos, avg_pos]), max([median_pos, avg_pos]) + 1):
#    fuel_values.append(sum_fuel(positions, pos, False))
#
#print(f'Day 2 : ', int(min(fuel_values)))

# actually it should be average value, but I'm not sure my average calculation is quite right
# test input needs average + 1 to work, whereas my input does not ; WTF ?
print('Day 2 : ', int(min([sum_fuel(positions, avg_pos, False), sum_fuel(positions, avg_pos + 1, False)])))
