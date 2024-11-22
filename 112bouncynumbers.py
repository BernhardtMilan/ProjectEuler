def isIncreasingNum(n):
    for i in range(len(str(n))-1):
        if int(str(n)[i]) > int(str(n)[i+1]):
            return False
    return True

def isDecreasingNum(n):
    for i in range(len(str(n))-1):
        if int(str(n)[i]) < int(str(n)[i+1]):
            return False
    return True

numofBouncy = 0
percent = 0
i = 0
while percent < 99:
    i+=1
    if isIncreasingNum(i):
        continue
    if isDecreasingNum(i):
        continue
    numofBouncy += 1
    percent = (numofBouncy/i)*100
    if percent.is_integer(): print(f"with number {i} we reach: {percent}%")