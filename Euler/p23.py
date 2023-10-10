# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is
# called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
# written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the greatest number that cannot be
# expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def sum_of_divisors(n):
    divs = []
    for x in range(1, n):
        if n % x == 0:
            divs.append(x)
    return sum(divs)


assert sum_of_divisors(12) == 16
assert sum_of_divisors(28) == 28


def is_abundant(n):
    sd = sum_of_divisors(n)
    if sd > n:
        return True
    return False


abundant_numbers = []
for x in range(0, 28124):
    if is_abundant(x):
        abundant_numbers.append(x)

sums = [0] * 28124
for x in range(0, len(abundant_numbers)):
    for y in range(x, len(abundant_numbers)):
        s = abundant_numbers[x] + abundant_numbers[y]
        if s <= 28123:
            if sums[s] == 0:
                sums[s] = s

total = sum(x for x in range(1, len(sums)) if sums[x] == 0)

print(total)
