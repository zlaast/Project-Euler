# Project Euler: Problem 1
# Multiples of 3 or 5

sum = 0
for number in range (3, 1000):
    if (number % 15 == 0 or number % 3 == 0 or number % 5 == 0): # if number is divisible by 15, then 3 or 5
        sum += number
print(sum)
