import math
#we have 20 right moves and 20 down moves, we have to use every one.
#so this becomes a permutation problem with reaccuring elements.

#n is the total number of moves
#k is the number of right moves
n = 40
k = 20
print(math.comb(n, k))