#!/usr/bin/env python3
import sys

coords = []
instr = []

max_x = 0
max_y = 0

# read file
found_empty = False
with open(sys.argv[1], 'r') as f:
    for l in f.readlines():
        if len(l) > 1:
            if found_empty:
                folding = l.rstrip().split('=')
                instr.append({'axis': folding[0][-1], 'value': int(folding[1])})
            else:
                coord = list(map(lambda x: int(x), l.rstrip().split(',')))
                max_x = max(max_x, coord[0])
                max_y = max(max_y, coord[1])
                coords.append(coord)
        else:
            found_empty = True

# make grid
grid = []
for y in range(0, max_y + 1):
    grid.append(['.'] * (max_x + 1))
for c in coords:
    grid[c[1]][c[0]] = '#'

def print_grid(g):
    for l in g:
        print(' '.join(l))
    print ('')

def count_pixels(grid):
    s = 0
    for l in grid:
        s += sum([1 for p in l if p == '#'])
    return s

def fold(grid, axis, coord):
    new_grid = []
    if axis == 'y':
        new_grid = grid[0:coord]
        offset = 0
        # if height is even, bottom line will appear "higher" than first line
        # once folded => we need to increase grid starting with a new empty line
        # note : theoritically we could fold at any position, and offset could be > 1
        #        but it seems the author of this puzzle decided not to do such nasty things :)
        if 2 * (coord + 1) <= len(grid):
            new_grid.insert(0, [ '.' ] * len(grid[0]))
            offset = 1
        y = len(grid) - 1
        while y > coord:
            yy = 2 * coord - y + offset
            for x in range(0, len(new_grid[yy])):
                if grid[y][x] == '#':
                    new_grid[yy][x] = '#'
            y -= 1
    elif axis == 'x':
        for l in grid:
            new_line = l[:coord]
            x = len(grid[0]) - 1
            while x > coord:
                offset = 0
                # same as horizontal folding : if width is even, we need a new empty column
                if 2 * (coord + 1) <= len(grid[0]):
                    new_line.insert(0, '.')
                    offset = 1
                xx = 2 * coord - x + offset
                if l[x] == '#':
                    new_line[xx] = '#'
                x -= 1
            new_grid.append(new_line)
    else:
        return grid

    return new_grid

part1_done = False
for i in instr:
    grid = fold(grid, i['axis'], i['value'])
    if not part1_done:
        print(f'Part 1 : {count_pixels(grid)}')
    part1_done = True

print('Part 2:')
print_grid(grid)
