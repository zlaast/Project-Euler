# Project Euler: Problem 6
# Sum square difference

n = 100

a = n*(n+1)
sum_square = (a*(2*n + 1))/6
square_sum = (a/2)**2

print(square_sum-sum_square)