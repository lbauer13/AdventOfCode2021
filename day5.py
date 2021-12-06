#!/usr/bin/env python3
import sys

# read file
vents = []
max_s = 0
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        points = line.rstrip().split()
        p1 = list(map(lambda x: int(x), points[0].split(',')))
        p2 = list(map(lambda x: int(x), points[2].split(',')))
        # get max size to create map
        max_s = max(p1 + p2 + [ max_s ])
        vents.append([p1, p2])

def print_map(m):
    for l in m:
        print(' '.join(map(lambda x: str(x), l)))
    print('')

def count_map(m):
    s = 0
    for l in m:
        s += sum([ 1 for i in l if i != '.' and i > 1 ])
    return s

def compute_map(m, vents, any_direction):
    for v in vents:
        # find how we move horizontally
        x_min = min([v[0][0], v[1][0]])
        x_max = max([v[0][0], v[1][0]])
        if v[0][0] > v[1][0]:
            x_off = -1
        else:
            if v[0][0] == v[1][0]:
                x_off = 0
            else:
                x_off = +1

        # same, vertically
        y_min = min([v[0][1], v[1][1]])
        y_max = max([v[0][1], v[1][1]])
        if v[0][1] > v[1][1]:
            y_off = -1
        else:
            if v[0][1] == v[1][1]:
                y_off = 0
            else:
                y_off = +1

        # how many steps : either x, y, or both
        steps = max([x_max - x_min, y_max - y_min])

        if (x_min == x_max) or (y_min == y_max) or any_direction:
            x = v[0][0]
            y = v[0][1]
            for z in range(0, steps + 1):
                if m[y][x] == '.':
                    m[y][x] = 1
                else:
                    m[y][x] += 1
                x += x_off
                y += y_off

            #print_map(m)
    return m

# make empty maps for part 1 and 2
vent_map = []
vent_map_any = []
for x in range(0, max_s + 1):
    line = [ '.' ] * (max_s + 1)
    vent_map.append(line)
    line_any = line.copy()
    vent_map_any.append(line_any)

vent_map = compute_map(vent_map, vents, False)
print ('Part 1 : ' + str(count_map(vent_map)))

vent_map_any = compute_map(vent_map_any, vents, True)
print ('Part 2 : ' + str(count_map(vent_map_any)))
