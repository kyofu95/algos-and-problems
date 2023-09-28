# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2^1000?


def calculate_power(n):
    power = 2
    for _ in range(1, n):
        power = 2 * power
    return power


def sum(n):
    power = calculate_power(n)
    sum = 0
    while power > 0:
        power, modulo = divmod(power, 10)
        sum = sum + modulo
    return sum


print(sum(1000))
