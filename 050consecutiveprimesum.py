def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(1000000):
    if is_prime(i):
        primes.append(i)

most = 1
num = 0
for i in range(len(primes)-1, 1, -1):
    j = 0
    while primes[j] < primes[i]/most:
        sum = primes[j]
        k = 0
        while primes[i] > sum and j+k < i:
            k += 1
            sum += primes[j+k]
            if primes[i] == sum and k > most:
                num = primes[i]
                most = k
        j+=1

print(most+1)
print(num)