def is_palindrome(n):
    if n < 10:
        return False
    s = str(n)
    return s == s[::-1]

def reversed(n):
    return int(str(n)[::-1])

def is_lychrel_number(n):
    i = 0
    sum = n + reversed(n)
    while i < 50:
        if is_palindrome(sum):
            return False
        i += 1
        sum = sum + reversed(sum)
    return True


sum = 0
for i in range(1, 10000):
    if is_lychrel_number(i):
        sum += 1

print(sum)