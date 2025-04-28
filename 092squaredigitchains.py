def square_sum_of_digits(n):
    sum = 0
    for num in str(n):
        sum += int(num)**2
    return sum

chain_89 = set({89})
chain_1 = set({1})

def is_in_chain(n):
    if n in chain_89:
        return True, 89
    if n in chain_1:
        return True, 1
    return False, None

for i in range(1, 10000000):
    n = i
    found, chain = is_in_chain(n)
    while not found:
        n = square_sum_of_digits(n)
        found, chain = is_in_chain(n)

    if chain == 89:
        chain_89.add(i)
    elif chain == 1:
        chain_1.add(i)

print(len(chain_89))