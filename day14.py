from collections import defaultdict, Counter

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

poly = list(data[0])
inserts = {}

# part 1
for line in data[2:]:
    x, y = line.split(' -> ')
    inserts[x] = y

for _ in range(10):
    i = 0
    while i < len(poly):
        pair = ''.join(poly[i:i+2])

        if pair not in inserts:
            i += 1
            continue

        insert = inserts[pair]
        poly.insert(i + 1, insert)
        i += 2

vals = Counter(poly).values()
ans = max(vals) - min(vals)
print('Part 1:', ans)

# part 2
for k, v in inserts.items():
    n1 = k[0] + v
    n2 = v + k[1]

    inserts[k] = (n1, n2)


poly = list(data[0])
polymap = defaultdict(int)
for i in range(1, len(poly)):
    k = poly[i -1] + poly[i]
    polymap[k] += 1

for _ in range(40):
    new = defaultdict(int)

    for k,v in polymap.items():
        p1, p2 = inserts[k]

        new[p1] += v
        new[p2] += v

    polymap = new

chars = defaultdict(int)
for k,v in polymap.items():
    a, b = k
    chars[a] += v
    chars[b] += v

chars[poly[0]] += 1
chars[poly[-1]] += 1

for k in chars.keys():
    chars[k] //= 2

ans = max(chars.values()) - min(chars.values())
print('Part 2:', ans)

