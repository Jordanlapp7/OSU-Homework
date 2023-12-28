# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/21/2023
# Description: Takes a file name of a .txt file containing one number on each line and writes the sum to a .txt file.

def file_sum(file_name):
    """Takes a file name of a .txt file containing one number on each line and writes the sum to a .txt file."""
    nums = []
    with open(file_name, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            nums.append(float(stripped_line))
    nums_sum = sum(nums)
    with open('sum.txt', 'w') as file:
        file.write(str(nums_sum))
