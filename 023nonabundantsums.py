def is_abundant(n):
    sum = 0
    for i in range(1, (int)(n**0.5) + 1): 
        if (n % i == 0): 
            if not (n / i == i or i == 1):
                sum += n // i
            sum += i
    return sum > n

list = []
evenlist = []
for i in range(28112):
    if is_abundant(i):
        if (i % 2 == 1):
            evenlist.append(i)
        list.append(i)

sum = 0
for i in range(28123):
    if (i % 12 == 0 and i > 12):
        continue
    if i % 2 == 0:
        found = False
        skip = False
        skip2 =  False
        j = 0
        while (not skip) and (not found) and (j < len(list)-1):
            if list[j] + 12 > i or i / list[j] < 2:
                skip = True
                continue
            skip2 = False
            k = j
            while (not skip2) and (not found) and (k < len(list)):
                #print(list[j], list[k])
                if list[j]+list[k] == i:
                    found = True
                if list[j]+list[k] > i:
                    skip2 = True
                    continue
                k+=1
            j += 1
        if not found:
            sum += i
    else:
        found = False
        for j in range(len(evenlist)):
            if i-evenlist[j] in list:
                found = True
        if not found:
            sum += i

print(sum)