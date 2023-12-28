# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/27/2023
# Description: Recursively returns true if list is strictly decreasing, else false.

def is_decreasing(list_num):
    """Recursively returns true if list is strictly decreasing, else false."""
    if len(list_num) == 1:
        return True
    if list_num[0] > list_num[1]:
        return is_decreasing(list_num[1:])
    else:
        return False
