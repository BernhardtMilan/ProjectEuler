def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    else:
        if n < 10:
            return True
        else:
            return right_truncatable_prime(n//10)

def left_truncatable_prime(n):
    if not is_prime(n):
        return False
    else:
        if n < 10:
            return True
        else:
            return left_truncatable_prime(int(str(n)[1:]))

def truncatable_prime(n):
    if not right_truncatable_prime(n):
        return False
    if not left_truncatable_prime(n):
        return False
    return True

numberOfPrimes = 0
primes = []
i = 10
while numberOfPrimes < 11:
    i += 1
    if truncatable_prime(i):
        primes.append(i)
        numberOfPrimes += 1

print(sum(primes))