#to speed things up we can search from the back, so if the number is not divisible by 20 we can throw it out, this speeds up the process
def isDevisableBy1to20(n):
    for i in range(20, 0, -1):
        if n % (i) != 0:
            return False
    return True

i = 1
while not isDevisableBy1to20(i):
    i+=1

print(i)