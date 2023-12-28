# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/16/2023
# Description: Insertion sorts a list of strings alphabetically.

def string_sort(string_list):
    """Insertion sorts a list of strings alphabetically."""
    for index in range(1, len(string_list)):
        value = string_list[index]
        pos = index - 1
        while pos >= 0 and string_list[pos].lower() > value.lower():
            string_list[pos + 1] = string_list[pos]
            pos -= 1
        string_list[pos + 1] = value
    return
