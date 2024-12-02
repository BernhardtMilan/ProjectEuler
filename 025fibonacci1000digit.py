f1 = 1
f2 = 2
i=3
while len(str(f2)) < 1000:
    i+=1
    temp = f2
    f2 = f2 + f1
    f1 = temp

print(f2)
print(i)