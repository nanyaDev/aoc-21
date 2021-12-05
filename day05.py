import re
from collections import defaultdict

with open('input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

coords = []
for line in data:
    point1, point2 = line.split(' -> ')

    x1, y1 = point1.split(',')
    x2, y2 = point2.split(',')

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    coords.append([x1, y1, x2, y2])

tracker = defaultdict(int)
for coord in coords:
    x1, y1, x2, y2 = coord

    if x1 != x2 and y1 != y2:
        xstep = 1 if x2 > x1 else -1
        ystep = 1 if y2 > y1 else -1
        
        for x, y in zip(range(x1, x2 + xstep, xstep), range(y1, y2 + ystep, ystep)):
            tracker[(x,y)] += 1

    if y1 == y2:
        start = min(x1, x2)
        end = max(x1, x2)

        for x in range(start, end + 1):
            tracker[(x, y1)] += 1

    if x1 == x2:
        start = min(y1, y2)
        end = max(y1, y2)

        for y in range(start, end + 1):
            tracker[(x1, y)] += 1

count = 0
for coord in tracker.keys():
    if tracker[coord] > 1:
        count += 1

print(count)






