import math

def num_of_divisors(n):
    num = 0
    for i in range(1, (int)(math.sqrt(n)) + 1): 
        if (n % i == 0): 
            if (n / i == i): 
                num = num + 1
            else:
                num = num + 2
    return num

triangle_number = 1
i = 1
while num_of_divisors(triangle_number) < 500:
    i+=1
    triangle_number += i

print(triangle_number)
print(num_of_divisors(triangle_number))