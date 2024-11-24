from num2words import num2words

sum = 0 
for i in range(1000):
    word = num2words(i+1)
    for char in word:
        if char.isalpha():
            sum += 1

print(sum)