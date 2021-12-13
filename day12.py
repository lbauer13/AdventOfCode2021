#!/usr/bin/env python3
import sys

segments = dict()

# read file
with open(sys.argv[1], 'r') as f:
    for l in f.readlines():
        s = l.rstrip().split('-')
        if s[1] != 'start' and s[0] != 'end':
            if s[0] in segments.keys():
                segments[s[0]].append(s[1])
            else:
                segments[s[0]] = [s[1]]
        if s[0] != 'start' and s[1] != 'end':
            if s[1] in segments.keys():
                segments[s[1]].append(s[0])
            else:
                segments[s[1]] = [s[0]]

# don't do next optimization for step 2
segments2 = segments.copy()

# don't come back in small caves => delete such segments
todel = []
for s in segments.keys():
    if segments[s][0] == segments[s][0].lower() and len(segments[s]) == 1 and s in segments[segments[s][0]]:
        todel.append(s)
for d in todel:
    del segments[d]

def route_has_dup(route):
    distinct_caves = []
    for cave in route:
        if cave == cave.lower() and cave not in ('start', 'end'):
            if cave in distinct_caves:
                return True
            else:
                distinct_caves.append(cave)
    return False

# recursive function to complete partial route with all possible other routes
def complete_routes(routes, with_one_dup):
    more = []
    found = False
    for r in routes:
        # this one is not finished, try next caves
        if r[len(r)-1] != 'end' and r[len(r)-1] in segments:
            for n in segments[r[len(r)-1]]:
                # add all uppercase caves, or lowercase cave if not already visited
                # for part 2, allow exactly one duplicate lowercase cave
                if n.lower() != n or n not in r or (with_one_dup and not route_has_dup(r)):
                    found = True
                    r2 = r.copy()
                    r2.append(n)
                    more.append(r2)
        # this one is finished
        else:
            more.append(r)
    if found:
        return complete_routes(more, with_one_dup)
    else:
        # return all routes from start to end
        res = []
        for r in more:
            if r[len(r)-1] == 'end':
                res.append(r)
        return res

def print_routes(routes):
    for r in routes:
        print(','.join(r))

all_routes = complete_routes([['start']], False)
#print_routes(all_routes)
print(f'Part 1 : {len(all_routes)}')

segments = segments2
all_routes = complete_routes([['start']], True)
#print_routes(all_routes)
print(f'Part 2 : {len(all_routes)}')
