# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def div_by_seq(num, seq):
    for i in seq:
        if num % i != 0:
            return False
    return True

def find_smallest(n):
    seq = range(1, n)
    number = 1
    while True:
        if div_by_seq(number, seq):
            return number
        number += 1

print(find_smallest(10))
print(find_smallest(20))