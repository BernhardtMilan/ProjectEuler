sumSquare = 0
squaresum = 0
for i in range(1, 101):
    sumSquare += i*i
    squaresum += i

squaresum = squaresum*squaresum

print(sumSquare)
print(squaresum)
print(squaresum-sumSquare)