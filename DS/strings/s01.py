# Two strings str1 and str2 are called isomorphic if there is a one-to-one mapping possible
# for every character of str1 to every character of str2. And all occurrences of every
# character in ‘str1’ map to the same character in ‘str2’.

# Examples:

#     Input:  str1 = “aab”, str2 = “xxy”
#     Output: True
#     Explanation: ‘a’ is mapped to ‘x’ and ‘b’ is mapped to ‘y’.

#     Input:  str1 = “aab”, str2 = “xyz”
#     Output: False
#     Explanation: One occurrence of ‘a’ in str1 has ‘x’ in str2 and other occurrence of ‘a’ has ‘y’.


def is_isomorphic(a, b):
    if len(a) != len(b):
        return False
    
    dictionary = {}
    
    for k, v in zip(a, b):
        last_value = dictionary.get(k)
        if last_value and last_value != v:
            return False
        dictionary[k] = v

    return True

assert is_isomorphic("aab", "xxy") == True
assert is_isomorphic("aab", "xyz") == False
assert is_isomorphic("egg", "add") == True