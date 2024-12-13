from itertools import permutations 

def are_permutes(x, y):
    if len(str(x)) == len(str(y)):
        return (sorted([int(a) for a in str(x)]) == sorted([int(a) for a in str(y)]))
    return False

cubes = []
for i in range(1000000):
    cubes.append(i**3)

for cube in cubes:
    count = 0
    for secound_cube in cubes:
        if len(str(secound_cube)) > len(str(cube)):
            break
        if are_permutes(cube, secound_cube):
            count+=1
    if count == 5:
        print(cube)
        quit()