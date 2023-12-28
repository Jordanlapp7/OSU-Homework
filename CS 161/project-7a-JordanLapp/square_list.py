# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/17/23
# Description: Takes a list of numbers and replaces each value with its square.

def square_list(nums_list):
    """Takes a list of numbers and replaces each value with its square."""
    for index in range(len(nums_list)):
        nums_list[index] = nums_list[index] ** 2
