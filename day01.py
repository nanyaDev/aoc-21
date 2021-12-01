with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    input = [int(num) for num in data]

count = 0

for i, n in enumerate(input):
    if (i >= len(input) - 3): 
        break
    if (n < input[i+3]):
        count += 1

print(count)
