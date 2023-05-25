# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def cond(a, b, c):
    if a**2 + b**2 == c**2:
        if a + b + c == 1000:
            return True
    return False

# def bruteforce_product():
#     for a in range(1, 1000):
#         for b in range(1, 1000):
#             for c in range(1, 1000):
#                 if cond(a, b, c):
#                     return a * b * c
#     raise RuntimeError("Could not find product!")

def bruteforce_product():
    # Slightly more optimal bruteforcing, since a + b + c == 1000
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000-a-b
            if cond(a, b, c):
                return a * b * c
    raise RuntimeError("Could not find product!")

print(bruteforce_product())