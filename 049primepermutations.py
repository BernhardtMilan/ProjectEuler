from itertools import permutations
import math
#csak szépíteni kell
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tuple_to_int(tup):
    return int(sum(math.pow(10, i) * int(num) for i, num in enumerate(reversed(tup))))

def is_permuates_3_primes(n):
    primepermutations = []
    for num in permutations(str(n), 4):
        if is_prime(tuple_to_int(num)):
            primepermutations.append(tuple_to_int(num))

    if ((n + 3330) in primepermutations) and ((n + 6660) in primepermutations):
        return True
        
    return False

fourdigitprimes = []
for i in range(1000, 10000):
    if is_prime(i):
        fourdigitprimes.append(i)

for i in range(len(fourdigitprimes)):
    if is_permuates_3_primes(fourdigitprimes[i]):
        if fourdigitprimes[i] != 1487:
            print(f"{fourdigitprimes[i]}{fourdigitprimes[i]+3330}{fourdigitprimes[i]+6660}")