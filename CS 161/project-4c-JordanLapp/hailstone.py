# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 4/26/2023
# Description: Returns how many steps in the hailstone sequence a number takes to reach 1.

def hailstone(num):
    """Returns how many steps in the hailstone sequence a number takes to reach 1."""
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            steps += 1
        else:
            num = num * 3 + 1
            steps += 1
    return steps
