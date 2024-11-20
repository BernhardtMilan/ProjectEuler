sum = 2

fib = [1,2]
while fib[-1] < 4000000:
    new = fib[-1] + fib[-2]
    if new % 2 == 0:
        sum += new
    fib.append(new)

print(sum)