# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/17/23
# Description: Takes a list and reverses the order of elements.

def reverse_list(any_list):
    """Takes a list and reverses the order of elements."""
    for index in range(len(any_list) // 2):
        any_list[index], any_list[len(any_list) - index - 1] = any_list[len(any_list) - index - 1], any_list[index]
