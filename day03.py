with open('input.txt', 'r') as f:
    data = f.readlines()
    data = [x.strip() for x in data]

gamma = ''
epsilon = ''

for i in range(len(data[0])):
    zeros = 0
    ones = 0

    for j in range(len(data)):
        if data[j][i] == '0':
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'


oxygen = data.copy()
co2 = data.copy()

for i in range(len(data[0])):
    zeros = 0
    ones = 0
    for j in range(len(oxygen)):
        if oxygen[j][i] == '0':
            zeros += 1
        else:
            ones += 1

    digit = '0' if zeros > ones else '1'

    if len(oxygen) > 1:
        prev = oxygen
        oxygen = []
        for j in range(len(prev)):
            if prev[j][i] == digit:
                oxygen.append(prev[j])

    zeros = 0
    ones = 0
    for j in range(len(co2)):
        if co2[j][i] == '0':
            zeros += 1
        else:
            ones += 1

    digit = '0' if zeros <= ones else '1'

    if len(co2) > 1:
        prev = co2
        co2 = []
        for j in range(len(prev)):
            if prev[j][i] == digit:
                co2.append(prev[j])

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
oxygen = int(*oxygen, 2)
co2 = int(*co2, 2)

print('Part 1: ', gamma * epsilon)
print('Part 2: ', oxygen * co2)

