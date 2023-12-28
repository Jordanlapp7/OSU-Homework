# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/8/23
# Description: Created a class to represent a person and function
# to calculate the standard deviation of a list of people.

class Person:
    """Represents a person with a name and age"""
    def __init__(self, name, age):
        """Creates a person with a name and age"""
        self._name = name
        self._age = age

    def get_age(self):
        """Returns the person's name"""
        return self._age


def avg(list_of_numbers):
    """Takes a list of numbers and returns the average"""
    return sum(list_of_numbers) / len(list_of_numbers)


def std_dev(list_of_people):
    """Takes a list of people and returns the standard deviation of their age"""
    ages = []
    for person in list_of_people:
        ages += [person.get_age()]
    avg_age = avg(ages)
    transformed_ages = [(x - avg_age) ** 2 for x in ages]
    variance = avg(transformed_ages)
    return variance ** 0.5
