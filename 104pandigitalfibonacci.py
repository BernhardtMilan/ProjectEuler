import math

f1 = 1
f2 = 1
i=2
found = False
while not found:
    i+=1
    temp = f2
    f2 = f2 + f1
    f1 = temp
    t = f2
    t = t // 10 ** (int(math.log(t, 10)) - 10 + 1)
    first = set((str(t)[:9]))
    if len(first) == 9:
        if '0' not in first:
            print(i)
            print(first)
            t = f2 % 1000000000
            last = set((str(t)[-9:]))
            if len(last) == 9:
                if '0' not in last:
                    found = True
print("this:")
print(i)

# we could use the idea that fibonaci numbers can be calculated by the golden ration, I will come back to this