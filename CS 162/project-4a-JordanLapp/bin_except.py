# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/16/2023
# Description: Completes a binary search, raises an error if not found.

class TargetNotFound(Exception):
    pass


def bin_except(a_list, target):
    """Searches for target in a_list, raises TargetNotFound error if not found."""
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound
