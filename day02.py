with open('input.txt', 'r') as f:
    data = f.readlines()

aim = 0
h = 0
v = 0

for line in data:
    dir, n = line.split()
    n = int(n)

    if dir == 'forward':
        h += n
        v += aim * n
    if dir == 'backward':
        h -=n
        v -= aim * n
    if dir == 'up':
        aim -= n
    if dir == 'down':
        aim += n

print(h * v)
