# Project Euler: Problem 24
# Lexicographic permutations

from itertools import permutations

lex = list(permutations([0,1,2,3,4,5,6,7,8,9]))

lex_string = []
for i in lex[999999]:
    lex_string.append(str(i))

print(''.join(lex_string))