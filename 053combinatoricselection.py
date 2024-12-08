def pascal_triangle(n): 
    full = [[1]]
    for x in range(1, n):
        level = [1]
        for y in range(1, x):
            level.append(full[x-1][y-1] + full[x-1][y])
        level.append(1)
        full.append(level)
    return full

pascals = pascal_triangle(101)

sum = 0
for row in pascals:
    for element in row:
        if element > 1000000:
            sum+=1

print(sum)