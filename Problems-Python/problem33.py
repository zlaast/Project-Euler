# Project Euler: Problem 33
# Digit Cancelling Fractions

from fractions import Fraction

prod = 1
for n in range(11, 100):
    for d in range(11, 100):
        if (n/d < 1):
            if n % 10 != 0 and d % 10 != 0:
                n_str = [int(i) for i in str(n)]
                d_str = [int(i) for i in str(d)]

                for i in n_str:
                    if i in d_str:
                        _n = n_str.copy()
                        _d = d_str.copy()
                        _n.remove(i)
                        _d.remove(i)

                        n_int = int(_n[0])
                        d_int = int(_d[0])

                        if (n/d == n_int/d_int):
                            prod *= n/d

print(Fraction('%.3f'%(prod)))
