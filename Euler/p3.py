# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def get_primes(num):
    primes = []
    p = 2
    while num:
        if num % p != 0:
            p += 1
            continue

        primes.append(p)

        num = num / p
        
        if num == 1:
            break
    return primes

print(get_primes(13195))
print(get_primes(600851475143))