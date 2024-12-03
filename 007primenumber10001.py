def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

ind = 0
i = 0
while ind < 10001:
    i+=1
    if is_prime(i): ind+=1

print(f"The {ind}th prime number is {i}") 