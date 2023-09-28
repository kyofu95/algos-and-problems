# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
# are 3+3+5+4+4=19 letters used in total.

# If all the numbers from 1
# to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# Note:  do not count spaces or hyphens.
#  For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
#  contains 20 letters. The use of “and” when writing out numbers is in compliance with British usage.


# zero was added for consistency
SPECIAL_DIGITS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

TENS = [
    None,
    None,
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def get_number_in_english(number: int):
    if number < 20:
        return SPECIAL_DIGITS[number]

    if number < 100:
        if number % 10 == 0:
            return TENS[number // 10]
        return TENS[number // 10] + SPECIAL_DIGITS[number % 10]

    if number < 1000:
        if number % 100 == 0:
            return SPECIAL_DIGITS[number // 100] + "hundred"

        return (
            SPECIAL_DIGITS[number // 100]
            + "hundredand"
            + get_number_in_english(number % 100)
        )

    if number == 1000:
        return "onethousand"


print(len(get_number_in_english(342)))
print(len(get_number_in_english(115)))
l_sum = [len(get_number_in_english(x)) for x in range(1, 5 + 1)]
print(sum(l_sum))
l_sum = [len(get_number_in_english(x)) for x in range(1, 1000 + 1)]
print(sum(l_sum))
