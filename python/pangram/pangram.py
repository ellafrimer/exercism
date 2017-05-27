"""
a pangram is a sentence that uses all the letters 
in the alphabet at least once
"""
def is_pangram(sentence):
    ABC_LEN = 26

    if len(sentence) < ABC_LEN:
        return False

    abc = {}

    for letter in sentence.lower():
        if letter.isalpha():
            abc[letter] = True

    return len(abc) == ABC_LEN





