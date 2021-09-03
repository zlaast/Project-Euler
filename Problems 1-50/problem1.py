# Project Euler: Problem 1
# Multiples of 3 or 5

sum = 0
for number in range (3, 1000):
    if (not number % 15 or not number % 3 or not number % 5): # if number is divisible by 15, then 3 or 5
        sum += number
print(sum)
