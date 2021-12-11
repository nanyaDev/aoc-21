from itertools import product

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')


for i in range(len(data)):
    data[i] = [int(n) for n in data[i]]

rn = len(data)
cn = len(data[0])

count = 0
n = 1
while True:
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] += 1

    flashed = []
    while True:
        prev = flashed.copy()
        for i in range(rn):
            for j in range(cn):
                if data[i][j] > 9 and (i,j) not in flashed:
                    flashed.append((i,j))

                    for di, dj in product((-1, 0, 1), repeat=2):
                        ii = i + di
                        jj = j + dj
                        if 0 <= ii < rn and 0 <= jj < cn:
                            data[ii][jj] += 1

        if len(prev) == len(flashed):
            count += len(flashed)
            n += 1

            for i,j in flashed:
                data[i][j] = 0

            break

        if len(flashed) == rn * cn:
            print(n)
            exit()

