def is_isogram(word):
    counts = {}

    for letter in word.lower():
        if letter in counts:
            return False
        elif letter.isalpha():
            counts[letter] = 1
    return True

