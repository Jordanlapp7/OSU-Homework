# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/27/2023
# Description: Recursively returns the maximum value in the list.

def list_max(num_list):
    """Recursively returns the maximum value in the list."""
    if len(num_list) == 1:
        return num_list[0]
    if num_list[0] <= num_list[1]:
        return list_max(num_list[1:])
    else:
        return list_max([i for x, i in enumerate(num_list) if x != 1])
