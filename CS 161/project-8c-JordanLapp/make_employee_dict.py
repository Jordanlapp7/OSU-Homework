# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 5/24/23
# Description: Creates an employee class and a function
# that creates employees and adds them to a dictionary.

class Employee:
    """Represents an employee with a name, id, salary, and email."""
    def __init__(self, name, id_number, salary, email_address):
        self._name = name
        self._id_number = id_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """Returns employees name"""
        return self._name

    def get_id_number(self):
        """Returns employees id number"""
        return self._id_number

    def get_salary(self):
        """Returns employees salary"""
        return self._salary

    def get_email_address(self):
        """Returns employees email"""
        return self._email_address


def make_employee_dict(names, id_nums, salaries, emails):
    """Takes lists of employee characteristics and creates an employee object for each index, adding each to a dictionary."""
    employees = {}
    for employee_num in range(len(names)):
        employees[id_nums[employee_num]] = Employee(names[employee_num], id_nums[employee_num], salaries[employee_num], emails[employee_num])
    return employees
