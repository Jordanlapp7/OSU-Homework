# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 4/26/2023
# Description: Returns the number at a specified position of the Fibonacci sequence.

def fib(pos):
    """Returns the number at a specified position of the Fibonacci sequence."""
    num = 1
    prev_num = 1
    while pos > 2:
        temp = num
        num += prev_num
        prev_num = temp
        pos -= 1
    return num
