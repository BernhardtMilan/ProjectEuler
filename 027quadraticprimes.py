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

def calculate_quardatic(a, b):
    num = 0
    result = b
    while is_prime(result):
        num += 1
        result = num*num + a*num + b
    return num

max = 0
a_max = 0
b_max = 0
for i in range(1001):
    for j in range(1001):
        for k in range(4):
            if k == 0:
                a = i
                b = j
            elif k == 1:
                a = i
                b = -j
            elif k == 2:
                a = -i
                b = j
            elif k == 3:
                a = -i
                b = -j
            current = calculate_quardatic(a, b)
            if current > max:
                max = current
                a_max = a
                b_max = b

print(a_max*b_max)