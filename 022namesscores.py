file_path = '0022_names.txt'

with open(file_path, 'r') as file:
    content = file.read()

names = content.replace('"', '').split(',')

def word_to_num(word):
    sum = 0
    for letter in word:
        sum += ord(letter)-64
    return sum

names = sorted(names)

sum = 0
for i in range(len(names)):
    sum += (i+1) * word_to_num(names[i])

print(sum)