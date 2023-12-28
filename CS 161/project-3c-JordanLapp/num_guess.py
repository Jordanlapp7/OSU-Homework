# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 4/19/2023
# Description: Prompts the user for an integer that the player will try to guess.

print("Enter the integer for the player to guess.")
num = int(input())
count = 0
guess = int
print("Enter your guess.")
while guess != num:
    guess = int(input())
    count += 1
    if guess > num:
        print("Too high - try again:")
    if guess < num:
        print("Too low - try again:")
print("You guessed it in", count, "tries.")
