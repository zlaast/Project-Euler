# Project Euler: Problem 9
# Special pythagorean triplet

# Euclid's Formula is used here. Check out https://en.wikipedia.org/wiki/Pythagorean_triple

for n in range (1, 1000):
    for m in range(n+1, 1000):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2

        if(a+b+c == 1000):
            print(a*b*c)
            break