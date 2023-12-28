# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 6/28/2023
# Description: Keeps track of students' names and grades and includes statistics for the group.

import statistics


class Student:
    """Contains a student's name and grade."""

    def __init__(self, name, grade):
        """Creates a student object with a name and grade."""
        self._name = name
        self._grade = grade

    def get_grade(self):
        """Returns the student's grade"""
        return self._grade


def basic_stats(students):
    """Takes a list of students and returns the mean, median, and mode of the grades as a tuple."""
    grades = []
    for student in students:
        grade = student.get_grade()
        grades.append(grade)
    mean = statistics.mean(grades)
    median = statistics.median(grades)
    mode = statistics.mode(grades)
    stats = (mean, median, mode)
    return stats
