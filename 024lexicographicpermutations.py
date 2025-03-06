from itertools import permutations 

print(int("".join(map(str, (list(list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[999999]))))))