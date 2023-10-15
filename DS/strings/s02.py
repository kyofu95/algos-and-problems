# Given a string s. The task is to check if it is Pangram or not.
#     A pangram is a sentence containing every letter in the English Alphabet.

# Examples:
#     Input: “The quick brown fox jumps over the lazy dog”
#     Output: is a Pangram
#     Explanation: Contains all the characters from ‘a’ to ‘z’]

#     Input: “The quick brown fox jumps over the dog”
#     Output: is not a Pangram
#     Explanation: Doesn’t contain all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing

from string import ascii_lowercase


def is_pangram(s: str):
    marks = [False] * 26

    s = s.lower().replace(" ", "")

    for letter in s:
        index = ascii_lowercase.index(letter)
        marks[index] = True

    return all(marks)


assert is_pangram("aThe quick brown fox jumps over the lazy dog") is True
assert is_pangram("The quick brown fox jumps over the dog") is False
