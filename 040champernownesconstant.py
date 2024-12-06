string = "0"
#we could calculate so the string does not get generated more then the 1000000th number. but it is sufficently fast this way
for i in range(190000):
    string += str(i+1)

pred = 1
for i in range(7):
    pred *= int(string[10**i])

print(pred)