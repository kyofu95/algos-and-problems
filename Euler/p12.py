# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

import math

def find_factors_length(n: int):
    factors = set()
    factors.update({n})
    for k in range(1, math.ceil(math.sqrt(n))+1):
        if n % k == 0:
            factors.update({k, n//k})

    return len(factors)

def get_triangle_number(n: int):
    return int(n*(n+1)/2)

def find_first_n_of_divisors():
    i = 1
    while True:
        tris = get_triangle_number(i)
        fac_length = find_factors_length(tris)
        if fac_length >= 500:
            return tris
        i += 1

print(find_first_n_of_divisors())