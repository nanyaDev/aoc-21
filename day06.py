from collections import defaultdict

with open('input.txt', 'r') as f:
    data = [int(n) for n in f.read().strip().split(',')]

fishes = defaultdict(int)
for fish in data:
    fishes[fish] += 1

for _ in range(256):
    zeros = fishes[0]

    for j in range(9):
        fishes[j] = fishes[j + 1] 
    
    fishes[8] = zeros
    fishes[6] += zeros

print(sum(fishes.values()))


