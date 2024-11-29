def get_divisors(n):
    yield n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i

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

def is_generating_integer(n):
    for divisor in get_divisors(n):
        if not is_prime(divisor + n // divisor):
            return False
    return True

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False
    return is_prime

limit = 100000000
primes = sieve(limit + limit // 2)
total_sum = 0
progress_interval = limit // 100
for i in range(2, limit + 1, 2):
    if i % progress_interval == 0:
        print(f"{i / limit * 100:.2f}%")
    if not primes[i + 1]:
        continue
    if not primes[i // 2 + 2]:
        continue
    if is_generating_integer(i):
        total_sum += i
print(total_sum + 1)