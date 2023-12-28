# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 4/11/2023
# Description: asks the user for a (integer) number of cents, from 0 to 99, and outputs how many
# of each type of coin would represent that amount with the fewest total number of coins.

print("Please enter an amount in cents less than a dollar.")
total = int(input())

q = total // 25
total -= q * 25
d = total // 10
total -= d * 10
n = total // 5
total -= n * 5
p = total // 1
total -= p * 1

print("Your change will be:")
print("Q:", q)
print("D:", + d)
print("N:", + n)
print("P:", + p)
