maxsum = 0
for a in range(1, 100):
    for b in range(1, 100):
        sum = 0
        num = pow(a, b)
        for i in range(len(str(num))):
            sum += int(str(num)[i])
        if sum > maxsum:
            maxsum = sum

print(maxsum)