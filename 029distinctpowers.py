combinations = set()

for i in range(2, 101):
    for j in range(2, 101):
        combinations.add((i**j))

print(len(combinations))