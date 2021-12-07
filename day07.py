with open('input.txt', 'r') as f:
    data = [int(n) for n in f.read().strip().split(',')]

fuels = []
for i in range(min(data), max(data)):
    fuel = 0
    for n in data:
        dis = abs(n - i)
        fuel += dis * (dis + 1) // 2

    fuels.append(fuel)

print(min(fuels))





