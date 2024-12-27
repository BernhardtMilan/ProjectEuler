prod = 1
for i in range(100):
    prod *= i+1

print(prod)
sum = 0
for i in range(len(str(prod))):
    sum += int(str(prod)[i])

print(sum)