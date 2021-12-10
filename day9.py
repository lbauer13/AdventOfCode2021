#!/usr/bin/env python3
import sys

grid = []

# read file
with open(sys.argv[1], 'r') as f:
    for l in f.readlines():
        grid.append(list(map(lambda x: int(x), l.rstrip())))

def print_grid(g, highlight, around=None):
    min_y = 0
    max_y = len(g)
    min_x = 0
    max_x = len(g[0])
    # only print around a point in the grid
    # to make visualisation easier in big grids
    if around:
        min_y = max([0, around[0] - 10])
        max_y = min([len(g), around[0] + 10])
        min_x = max([0, around[1] - 10])
        max_x = min([len(g[0]), around[1] + 10])
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            if [y,x] in highlight:
                color = '\033[1m\033[95m';
            else:
                color = '\033[96m';

            print(f'{color}{g[y][x]}\033[0m ', end = '')
        print('')

def find_lowpoints(g):
    lowpoints = {'coords': [], 'values': []}
    for y in range(0, len(g)):
        for x in range(0, len(g[y])):
            neigh = []
            val = g[y][x]
            # up
            if y > 0:
                neigh.append(g[y-1][x])
            # down
            if y < len(g) - 1:
                neigh.append(g[y+1][x])
            # left
            if x > 0:
                neigh.append(g[y][x-1])
            # right
            if x < len(g[y]) - 1:
                neigh.append(g[y][x+1])
            
            lower = [ v for v in neigh if v <= val ]
            if len(lower) == 0:
                lowpoints['coords'].append([y,x])
                lowpoints['values'].append(val)

    return lowpoints

def find_basin(g, point):
    points = [ point ]
    found = True
    # enlarge your basin... until you no longer find new points
    while found:
        found = False
        for p in points:
            # up
            if p[0] > 0 and [p[0]-1,p[1]] not in points and g[p[0]-1][p[1]] != 9 and g[p[0]-1][p[1]] > g[p[0]][p[1]]:
                found = True
                points.append([p[0]-1, p[1]])
            # down
            if p[0] < len(g) - 1 and [p[0]+1,p[1]] not in points and g[p[0]+1][p[1]] != 9 and g[p[0]+1][p[1]] > g[p[0]][p[1]]:
                found = True
                points.append([p[0]+1, p[1]])
            # left
            if p[1] > 0 and [p[0],p[1]-1] not in points and g[p[0]][p[1]-1] != 9 and g[p[0]][p[1]-1] > g[p[0]][p[1]]:
                found = True
                points.append([p[0], p[1]-1])
            # right
            if p[1] < len(g[p[0]]) - 1 and [p[0],p[1]+1] not in points and g[p[0]][p[1]+1] != 9 and g[p[0]][p[1]+1] > g[p[0]][p[1]]:
                found = True
                points.append([p[0], p[1]+1])
    return (points)

lowp = find_lowpoints(grid)
print('Part 1 : ' + str(sum(lowp['values']) + len(lowp['values'])))
#print_grid(grid, lowp['coords'])
#print('')

sizes = []
for p in lowp['coords']:
    b = find_basin(grid, p)
    sizes.append(len(b))
    #print_grid(grid, b, p)
    #print('')
sizes.sort(reverse=True)

print(f'Part 2 : {sizes[0] * sizes[1] * sizes[2]}')
