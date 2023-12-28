# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/8/23
# Description: Function takes a list of numbers and returns the statistical median.

def find_median(list_of_numbers):
    """Takes a list of numbers and returns the median"""
    sorted_list = sorted(list_of_numbers)
    if len(sorted_list) % 2 == 0:
        # Returns median of list with even number of elements.
        value_1 = sorted_list[int(len(sorted_list) / 2 - 1)]
        value_2 = sorted_list[int(len(sorted_list) / 2)]
        avg = (value_1 + value_2) / 2
        return avg
    # Returns median of list with odd number of elements
    return sorted_list[len(sorted_list) // 2]
