def sum_of_divisors(n):
    sum = 0
    for i in range(1, (int)(n**0.5) + 1): 
        if (n % i == 0): 
            if not (n / i == i or i == 1):
                sum += n // i
            sum += i
    return sum

list = [0]
sum = 0
list2 = []
for i in range(1, 10000):
    divsum = sum_of_divisors(i)
    list.append(divsum)
    if len(list) > divsum:
        if list[divsum] == i and divsum != i:
            sum += i + divsum
            list2.append((i, divsum))

print(sum)
print(list2)