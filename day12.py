from collections import defaultdict, Counter

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

def checkValid(p):
    path = [cave for cave in p if 'a' <= cave[0] <= 'z']
    counts = Counter(path)

    freq = list(counts.values())
    if freq.count(2) > 1:
        return False

    for f in freq:
        if f > 2:
            return False

    if counts['start'] > 1 or counts['end'] > 1:
        return False

    return True

cn = defaultdict(list)
paths = set()
paths.add(('start',))

for line in data:
    a, b = line.split('-')

    cn[a].append(b)
    cn[b].append(a)


while True:
    prev = paths.copy()
    paths = set()

    for path in prev:
        if path[-1] == 'end':
            paths.add(path)
            continue

        for c in cn[path[-1]]:
            new = path + (c,)

            if checkValid(new):
                paths.add(new)

    if len(prev) == len(paths):
        break

print(len(paths))

