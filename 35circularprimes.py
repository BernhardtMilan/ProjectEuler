def circulate(n):
    m = str(n)
    allPrime = True
    for i in range(len(m)):
        k = m[i:] + m[:i]
        allPrime = allPrime and is_prime(int(k))
    return allPrime

def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:
            return False

    return True

num = 0
for i in range(1000000):
    if circulate(i):
        num += 1

print(num)