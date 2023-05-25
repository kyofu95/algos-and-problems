# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def find_sum_of_primes(n: int):
    a = [True] * n
    sum = 0
    for i in range(2, n):
        if a[i]:
            sum = sum + i
            for j in range(i**2, n, i):
                a[j] = False
    return sum

print(find_sum_of_primes(2_000_000))