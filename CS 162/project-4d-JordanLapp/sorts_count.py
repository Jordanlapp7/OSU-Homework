# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/16/2023
# Description: Counts comparisons and exchanges for bubble and insertion sort.

def bubble_count(a_list):
    """Sorts a_list in ascending order while tracking comparisons and exchanges."""
    comparisons = 0
    exchanges = 0
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            comparisons += 1
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp
                exchanges += 1
    stats = (comparisons, exchanges)
    return stats


def insertion_count(a_list):
    """Sorts a_list in ascending order while tracking comparisons and exchanges."""
    comparisons = 0
    exchanges = 0
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
            comparisons += 1
            exchanges += 1
        a_list[pos + 1] = value
    stats = (comparisons, exchanges)
    return stats
