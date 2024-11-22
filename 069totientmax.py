import math 
 
def num_of_relatively_prime_integers(n): 
    if n <= 0: 
        return 0
 
    relatively_prime_numbers = 0
    for i in range(1, n): 
        if math.gcd(n, i) == 1: 
            relatively_prime_numbers += 1
 
    return relatively_prime_numbers

max = 0
maxplace = 0
for i in range(2, 1000001):
    #let me just boldly assume that it is divisible by the 4 smallest primes, so to reduce runtime
    if i % 2 != 0:
        continue
    if i % 3 != 0:
        continue
    if i % 5 != 0:
        continue
    if i % 7 != 0:
        continue
    num = i/num_of_relatively_prime_integers(i)
    if num > max:
        max = num
        maxplace = i
    if i % 1000 == 0:
        print(f"{i/10000}%")

print("max:")
print(maxplace)