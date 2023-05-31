# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

datasum = 0
with open("p13_nums", "r") as file:
    for line in file:
        datasum += int(line.strip())

print(str(datasum)[:10])