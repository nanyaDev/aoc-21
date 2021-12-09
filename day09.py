from collections import deque

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')
    data = [list(line.strip()) for line in data]

risk = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        low = True
        val = int(data[i][j])
        for di, dj in [(-1,0), (1,0), (0,1), (0,-1)]:
            ii = i + di
            jj = j + dj

            if ii < 0 or ii >= len(data) or jj < 0 or jj >= len(data[i]):
                continue

            adj = int(data[ii][jj])
            if val >= adj:
                low = False

        if low:
            risk += 1 + val

print('Part 1:', risk)

q = deque()
basins = []

for x in range(len(data)):
    for y in range(len(data[i])):
        if (x,y) in [coord for basin in basins for coord in basin]:
            continue

        if int(data[x][y]) == 9:
            continue

        basin = set([(x, y)])
        q.append((x, y))
        
        while q:
            i, j = q.popleft()

            val = int(data[i][j])
            for di, dj in [(-1,0), (1,0), (0,1), (0,-1)]:
                ii = i + di
                jj = j + dj

                if ii < 0 or ii >= len(data) or jj < 0 or jj >= len(data[i]):
                    continue

                if (ii, jj) in basin:
                    continue

                adj = int(data[ii][jj])
                if adj != 9:
                    q.append((ii, jj))
                    basin.add((ii, jj))

        basins.append(basin)

l = [len(basin) for basin in basins]
l.sort()

print('Part 2:', l[-3] * l[-2] * l[-1])




        



