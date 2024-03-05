# Project Euler: Problem 20
# Factorial digit sum

from math import factorial as f

number = f(100)
number_list = [int(i) for i in str(number)]
print(sum(number_list))