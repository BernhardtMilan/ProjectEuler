def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_n_digit_pandigital(n):
    s = set((str(n)))
    if len(str(n)) != len(s):
        return False
    example_set = set()
    for i in range(len(str(n))):
        example_set.add(str(i+1))
    if s != example_set:
        return False
    return True

#8 and 9 digit pandigital numbers cant be prime, because they all will be divisible by 9
#we can also leave out all the even numbers
#if we search from the back we can stop at the first, this will be the largest
for i in range(9999999, 0, -2):
    if is_n_digit_pandigital(i):
        if is_prime(i):
            print(i)
            break