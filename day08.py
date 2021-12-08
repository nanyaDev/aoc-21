with open('input.txt', 'r') as f:
    data = f.readlines()

count = 0
for line in data:
    d, o = line.split(' | ')
    d = d.strip().split()
    o = o.strip().split()

    h = {}
    for digit in d:
        if len(digit) == 2:
            h[1] = digit
        if len(digit) == 3:
            h[7] = digit
        if len(digit) == 4:
            h[4] = digit
        if len(digit) == 7:
            h[8] = digit

    for digit in d:
        if len(digit) == 6:
            if set(h[4]).issubset(digit):
                h[9] = digit
            elif set(h[1]).issubset(digit):
                h[0] = digit
            else:
                h[6] = digit

    for digit in d:
        if len(digit) == 5:
            if set(h[1]).issubset(digit):
                h[3] = digit
            elif set(digit).issubset(h[6]):
                h[5] = digit
            else:
                h[2] = digit
    
    output = ''
    for digit in o:
        for i in range(10):
            if set(digit) == set(h[i]):
                output += str(i)
    
    count += int(output)

print(count)




