# Project Euler: Problem 4
# Largest Palindrome Product

max = 0
product = 0
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        product = num1*num2

        if (str(product) == str(product)[::-1]):
            if (product > max):
                max = product
print(max)

        