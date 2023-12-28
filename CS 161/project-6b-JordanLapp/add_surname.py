# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/8/23
# Description: Takes a list of names and returns a list of only those that start
# with a "K" with "Kardashian" added to each one.

def add_surname(list_of_strings):
    """Takes a list of names and returns a list of those starting with a K with Kardashian added to each"""
    k_names = []
    for name in list_of_strings:
        if name[0] == "K":
            k_names += [name + " Kardashian"]
    return k_names
