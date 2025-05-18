import math

triangulars = []

for i in range(1000000):
    triangulars.append(int(i*(i+1)/2))

def is_perfect_square(num):
    root = int(math.sqrt(num))
    return root * root == num

def is_triangle_number(n):
    discriminant = 1 + 8 * n
    if not is_perfect_square(discriminant):
        return False
    x = (-1 + math.sqrt(discriminant)) / 2
    return x.is_integer()

def is_pentagonal_number(n):
    discriminant = 1 + 24 * n
    if not is_perfect_square(discriminant):
        return False
    x = (1 + math.sqrt(discriminant)) / 6
    return x.is_integer()

def is_hexagonal_number(n):
    discriminant = 1 + 8 * n
    if not is_perfect_square(discriminant):
        return False
    x = (1 + math.sqrt(discriminant)) / 4
    return x.is_integer()

i = 0
found = False
while not found:
    i += 1
    if i % 1000000 == 0:
        print(i)
    if is_pentagonal_number(triangulars[i]):
        if is_hexagonal_number(triangulars[i]):
            print(triangulars[i])
            if i > 285:
                found = True