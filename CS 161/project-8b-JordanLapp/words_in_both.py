# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/24/23
# Description: Takes two strings and returns a set of words that appear in both.

def words_in_both(string_one, string_two):
    """Takes two strings and returns a set of words that appear in both."""
    lower_one, lower_two = string_one.lower(), string_two.lower()
    list_one, list_two = lower_one.split(), lower_two.split()
    common_words = set()
    for word in list_one:
        if word in list_two:
            common_words.add(word)
    return common_words
