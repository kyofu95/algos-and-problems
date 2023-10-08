# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

# What is the total of all the name scores in the file?

from string import ascii_uppercase

with open("data/0022_names.txt", "r") as file:
    names = file.read()

names = [name.strip('"') for name in names.split(",")]
names.sort()


def count_letters(name):
    return sum(ascii_uppercase.index(letter) + 1 for letter in name)


assert count_letters("COLIN") == 53

total_score = 0
for pos, name in enumerate(names, 1):
    score = count_letters(name) * pos
    total_score += score

print(total_score)
