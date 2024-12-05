file_path = '0042_words.txt'

with open(file_path, 'r') as file:
    content = file.read()

words = content.replace('"', '').split(',')

def word_to_num(word):
    sum = 0
    for letter in word:
        sum += ord(letter)-64
    return sum

triange_numbers = []
for i in range(1, 50):
    triange_numbers.append(int(0.5*i*(i+1)))

count = 0
for word in words:
    if word_to_num(word) in triange_numbers:
        count += 1

print(count)