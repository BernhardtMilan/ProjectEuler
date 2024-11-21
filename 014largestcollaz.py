longest = 0
num = 0
for i in range(1, 1000000):
    len = 0
    j = i
    while j != 1:
        if j % 2 == 0:
            j = j/2
        else:
            j = 3*j + 1
        len+=1
    if len > longest:
        longest = len
        num = i
print(num)