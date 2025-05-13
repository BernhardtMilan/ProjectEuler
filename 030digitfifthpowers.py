sum_all = 0
#9 to the 5th power can only go up to 6 digits, even if the add it 7 times we only get a 6 digit number so 9^5 * 6 will be the max which is around 350000
for i in range(10, 350000):
    powers = [int(num)**5 for num in  str(i)]
    if i == sum(powers):
        print(i)
        sum_all += i

print(sum_all)