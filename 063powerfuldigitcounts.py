sum = 0
#10 to the n-th power is n+1 digits long, so any number above 9 will never be good
for i in range (1, 10):
    for j in range(1, 30):
        if j == len(str(i**j)):
            sum += 1
            #print(f"{i}^{j}={i**j} which is {j} digit long")

print(sum)