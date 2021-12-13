with open('input.txt', 'r') as f:
    data = f.readlines()

pts = set()

points = []
folds = []
flag = True
for line in data:
    if line == '\n':
        flag = False
        continue

    if flag:
        points.append(line.strip())
    else:
        axis, n = line.strip().split()[-1].split('=')
        folds.append((axis,int(n)))

for line in points:
    x, y = line.split(',')
    coord = (int(x), int(y))
    pts.add(coord)

for fold in folds:
    axis, n = fold

    i = 0 if axis == 'x' else 1

    ret = set()
    for p in pts:
        if p[i] <= n:
            ret.add(p)
            continue

        x, y = p

        if axis == 'x':
            x = n - (x - n)
        else:
            y = n - (y - n)

        ret.add((x,y))

    pts = ret

print(len(pts))

X = max([x for x,y in pts])
Y = max([y for x,y in pts])

for j in range(Y + 1):
    for i in range(X + 1):
        if (i,j) in pts:
            print('#', end='')
        else:
            print('.', end='')
    print('\n', end='')

