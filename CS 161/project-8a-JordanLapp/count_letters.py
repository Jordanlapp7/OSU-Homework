# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/24/23
# Description: Takes a string and returns a dictionary that
# tabulates how many of each letter is in that string.

def count_letters(phrase):
    """Takes a string and returns a dictionary that tabulates how many of each letter is in that string."""
    all_upper = phrase.upper()
    alphabet = {
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    }
    count = {}
    for letter in all_upper:
        if (letter in alphabet) & (letter not in count):
            count[letter] = 1
        elif letter in alphabet:
            count[letter] += 1
    return count
