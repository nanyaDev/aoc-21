from copy import deepcopy

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

for i in range(len(data)):
    data[i] = [int(n) for n in data[i]]

def getRisk(data):
    ret = deepcopy(data)
    for i in range(len(ret)):
        for j in range(len(ret[0])):
            ret[i][j] = 9 * len(ret) + 9 * len(ret[0])

    ret[0][0] = 0

    while True:
        prev = deepcopy(ret)
        for i in range(len(ret)):
            for j in range(len(ret[0])):
                for di, dj in ((0,1), (0,-1), (1,0), (-1,0)):
                    ii = i + di
                    jj = j + dj

                    if ii < 0 or ii >= len(ret) or jj < 0 or jj >= len(ret):
                        continue
                    
                    risk = ret[ii][jj] + data[i][j] 
                    if risk < ret[i][j]:
                        ret[i][j] = risk
        if prev == ret:
            return ret[-1][-1]

print('Part 1:', getRisk(data))


r = len(data)
c = len(data[0])
bigdata = [[None for x in range(5 * c)] for y in range(5 * r)]
for x in range(5 * r):
    for y in range(5 * c):
        i = x % r
        j = y % c
        n = x // r + y // c

        val = (data[i][j] + n)
        bigdata[x][y] = val if val <= 9 else val % 9

print('Part 2:', getRisk(bigdata))



                

