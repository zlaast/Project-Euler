# Project Euler: Problem 15
# Lattice paths

def paths(m, n, memo={}, ran=False):

    key = str(m) + ',' + str(n)
    if (key in memo):
        return memo[key]

    # Edge cases
    if m == 0 and n > 0:
        return n
    
    if m > 0 and n == 0:
        return m
    
    if m <= 0 or n <= 0:
        return 0
        
    # Normal operation
    if not ran:
        m += 1
        n += 1

    if m == 1 or n == 1:
        return 1

    memo[key] = paths(m-1, n, memo, True) + paths(m, n-1, memo, True)
    return memo[key]

print(paths(20, 20))