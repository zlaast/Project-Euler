# Project Euler: Problem 9
# Special Pythagorean Triplet

# Euclid's Formula is used here. 
# Check out https://en.wikipedia.org/wiki/Pythagorean_triple

for n in range (1, 500):
    for m in range(n+1, 500):
        if (m*(m+n) == 500):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2

            print(a*b*c)
            break