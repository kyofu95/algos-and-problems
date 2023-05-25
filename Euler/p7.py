# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def find_prime(c):
    position = 0
    i = 0
    while True:
        if is_prime(i):
            position += 1
            if position == c:
                return i
        i += 1

print(find_prime(10001))