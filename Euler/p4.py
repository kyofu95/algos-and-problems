# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_pal(num: int) -> bool:
    return str(num) == str(num)[::-1]

max_pal = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        number = i * j
        if is_pal(number):
            max_pal = max(max_pal, number)

print(max_pal)