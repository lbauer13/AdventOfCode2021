#!/usr/bin/env python3
import sys

grid = []

# read file
with open(sys.argv[1], 'r') as f:
    for l in f.readlines():
        grid.append(list(map(lambda x: int(x), list(l.rstrip()))))

# copied from part 9
def print_grid(g, highlight):
    for y in range(0, len(g)):
        for x in range(0, len(g[y])):
            if [y,x] in highlight:
                color = '\033[1m\033[95m';
            else:
                color = '\033[96m';

            print(f'{color}{g[y][x]}\033[0m ', end = '')
        print('')
    print('')

def evolve(g):
    # first step : increment energy level
    for y in range(0, len(g)):
        for x in range(0, len(g[y])):
            g[y][x] += 1
    # second step : make them flash
    flashed = []
    found_flash = False
    first_pass = True
    while found_flash or first_pass:
        first_pass = False
        found_flash = False
        for y in range(0, len(g)):
            for x in range(0, len(g[y])):
                # only flash once
                if g[y][x] > 9 and [y,x] not in flashed:
                    found_flash = True
                    flashed.append([y,x])
                    # increment adjacent cells
                    for yy in range(max([0, y-1]), min([len(g), y+2])):
                        for xx in range(max([0, x-1]), min([len(g[y]), x+2])):
                            if xx != x or yy != y:
                                g[yy][xx] += 1
    # last step : reset flashed to 0
    for f in flashed:
        g[f[0]][f[1]] = 0
    return flashed

part_1 = 0
step = 0
for s in range(0, 100):
    f = evolve(grid)
    step += 1
    part_1 += len(f)

print(f'Part 1 : {part_1}')

while len(f) < (len(grid) * len(grid[0])):
    f = evolve(grid)
    step += 1

print(f'Part 2 : {step}')
