sum = 0
for i in range(1000):
    if i % 3 == 0:
        sum += i
        continue
    if i % 5 == 0:
        sum += i
        continue
print(sum)