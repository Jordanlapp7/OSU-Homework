# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/3/23
# Description: Recursive function that takes two positive
# integers and returns the product of those two numbers.

def multiply(num_1, num_2):
    """Takes two positive integers and recursively finds their product"""
    if num_2 == 1:
        return num_1
    return num_1 + multiply(num_1, num_2 - 1)
