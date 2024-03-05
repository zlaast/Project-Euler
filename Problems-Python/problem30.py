# Project Euler: Problem 29
# Distinct Powers

n = 5
b = 10
maxnum = n*(b-1)**n
sum5th = 0

for number in range(2, maxnum):
    num = [int(i) for i in str(number)]

    narc = 0
    for i in num:
        narc += i**n

    if narc > maxnum:
        break

    if narc == number:
        sum5th += number

print(sum5th)