#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AoC: Day 6."""
from copy import copy
import sys


def get_input(file):
    """Get formatted input from the file."""
    ret = []
    with open(file) as filep:
        ret = list(map(int, filep.readline().rstrip().split(",")))

    return ret


# Bad ways to do this!
#
# def find_ages(days=80):
#     """Find the total number of fish one fish can create for each age."""
#     ret = {}
#     school = [1]

#     for day in range(0, days):
#         newlist = []
#         for index, fish in enumerate(school):
#             if fish == 0:
#                 newlist.append(8)
#                 school[index] = 6
#             else:
#                 school[index] -= 1
#         school += newlist
#         age = days - day
#         if age < 6:
#             ret[age] = len(school)

#     return ret


# def find_total(age, days=80):
#     """Find the total number of fish one fish starting at given age can create."""
#     newages = [age]

#     for _ in range(0, days):
#         newlist = []
#         for index, fish in enumerate(newages):
#             if fish == 0:
#                 newlist.append(8)
#                 newages[index] = 6
#             else:
#                 newages[index] -= 1
#         newages += newlist

#     return len(newages)


# def find_total_recursive(age, days):
#     """Do things."""
#     total = 1
#     for day in range(days, 0, -1):
#         if age == 0:
#             total += find_total_recursive(8, day - 1)
#             age = 7
#         age -= 1

#     return total


def count_school(data):
    """Count the ages of the fish in the school."""
    school = []
    for age in range(0, 9):
        school.append(0)

    for fish in data:
        school[fish] += 1

    return school


def solution1(school, days=80):
    """Find the total number of fish one fish starting at given age can create."""
    data = copy(school)

    for day in range(0, days):
        newfish = data[0]
        for age in range(1, 9):
            data[age - 1] = data[age]
        data[6] += newfish
        data[8] = newfish

    total = 0
    for age in data:
        total += age

    return total


def solution2(ages):
    """Find solution 2."""

    return 0


def main():
    """Execute the script."""
    ages = get_input("input.txt")
    school = count_school(ages)
    answer = solution1(school)
    print(f"Problem 1: answer: {answer}")
    answer = solution1(school, 256)
    print(f"Problem 2: answer = {answer}")

    return 0


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
