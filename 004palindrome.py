def isPalindrome(n):
    for i in range(len(str(n))//2 + 1):
        if str(n)[i] != str(n)[-(i+1)]:
            return False
    return True

largestPalidromeFound = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        if isPalindrome(i*j):
            if i*j > largestPalidromeFound:
                largestPalidromeFound = i*j

print(largestPalidromeFound)