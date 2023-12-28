# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 4/26/2023
# Description: Function takes the time in seconds as an argument and returns
# the distance in meters that the object has fallen in that time.

def fall_distance(t):
    """Takes in time as an argument and returns the distance in meters the object has fallen in that time."""
    return 0.5 * 9.8 * t ** 2
