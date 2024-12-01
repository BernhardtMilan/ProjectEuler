def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

sum = 0
for i in range(1000000):
    if is_palindrome(i):
        if is_palindrome(decimal_to_binary(i)):
            sum += i

print(sum)