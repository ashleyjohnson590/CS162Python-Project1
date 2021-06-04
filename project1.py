#Author: Ashley Johnson
#Date: 3/28/2021
#Description: Program takes a list of student objects as a parameter and returns a tuple containing mean, median, and mode.

import statistics

class Student:
    """Class initializes 2 private data members, student name and grade."""
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    """returns student grade"""
    def get_grade(self):
        return self._grade

def basic_stats(student_list):
    """calculates the mean, median, and mode of a list of Student objects using
    the statistics module."""
    grade = []

    for student in student_list:
        grade.append(student.get_grade())

    mean = statistics.mean(grade)
    median = statistics.median(grade)
    mode = statistics.mode(grade)
    return (mean, median, mode)