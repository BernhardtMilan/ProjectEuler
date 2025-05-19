def contain_the_same_digits(n, m):
    return sorted(str(n)) == sorted(str(m))

found = False
i = 1000
while not found:
    i += 1
    if int(str(i)[0]) > 1:
        i += 10**(len(str(i))-1) * 9
    if int(str(i)[1]) >= 7:
        i += 10**(len(str(i))-2) * 3
    if int(str(i)[2]) >= 7:
        i += 10**(len(str(i))-3) * 3
    if contain_the_same_digits(i, 2*i):
        j = 2*i
        possible = True
        print(i)
        while possible and j <= 5*i:
            j += i
            possible = possible and contain_the_same_digits(i, j)
        if possible:
            found = True
            print(i)