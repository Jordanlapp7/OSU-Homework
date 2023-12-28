# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 4/19/2023
# Description: asks the user to list a number of integers of their choosing and outputs the min/max of the integers.

print("How many integers would you like to enter?")
numInts = int(input())

print("Please enter", numInts, "integers.")

num = int(input())
min = max = num

while numInts > 1:
    num = int(input())
    if num < min:
        min = num
    if num > max:
        max = num
    numInts -= 1
print("min:", min)
print("max:", max)
