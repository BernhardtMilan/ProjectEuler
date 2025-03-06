def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def can_be_written(n):
    for i in range(n):
        if is_prime(i):
            for j in range(n):
                if n == i + 2*j*j:
                    return True
    return False

def is_composite(n):
    if n <= 1:
        return False
    return not is_prime(n)

for i in range(1, 100001, 2):
    if is_composite(i):
        if not can_be_written(i):
            print(i)
            break