with open('input.txt', 'r') as f:
     data = f.read().strip().split('\n')

scores1 = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }

scores2 = {
            '(': 1,
            '[': 2,
            '{': 3,
            '<': 4,
          }

pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
            '>': '<'
        }

ret1 = 0
ret2 = []
for line in data:
    stack = []
    illegal = False

    for ch in line:
        if ch in '([{<':
            stack.append(ch)

        if ch in ')]}>':
            if pairs[ch] != stack.pop() :
                ret1 += scores1[ch]
                illegal = True
                break

    if not illegal and stack:
        stack.reverse()

        sc = 0
        for ch in stack:
            sc *= 5
            sc += scores2[ch]

        ret2.append(sc)

print('Part 1:', ret1)

ret2.sort()
print('Part 2:', ret2[len(ret2) // 2])





