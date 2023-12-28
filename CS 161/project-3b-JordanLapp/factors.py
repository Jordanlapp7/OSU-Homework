# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 4/19/2023
# Description: asks the user for a positive integer and outputs the factors.

integer = int(input("Please enter a positive integer: "))
print("The factors of", integer, "are:")
for num in range(1, integer + 1):
    if integer % num == 0:
        print(num)
