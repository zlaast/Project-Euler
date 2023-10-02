# Project Euler: Problem 1
# Multiples of 3 or 5

sum = 0
for number in range (3, 1000):
    # if number is divisible by 3 or 5
    if (number % 3 == 0 or number % 5 == 0):
        sum += number
        
print(sum)